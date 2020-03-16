from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,View
from memberships.models import Membership,UserMembership,Subscription
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(user_membership = get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None

def get_selected_membership(request):
    membership_type =  request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None

class MembershipSelectView(ListView):
    template_name = 'memberships/membership_list.html'
    context_object_name = 'memberships'
    model = Membership

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self,request,*args,**kwargs):
        selected_membership_type = request.POST.get('membership_type')

        user_membership = get_user_membership(self.request)
        user_subscription = get_user_subscription(self.request)

        selected_membership_qs = Membership.objects.filter(membership_type=selected_membership_type)
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()

        """
        Validation to check if user memberships == selected_membership
        """
        if user_membership.membership == selected_membership:
            if user_subscription != None:
                messages.info(request, 'The selected membership is your current Memberships, your next payment would be due by {}'.format('get this value from stripe'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # PASS THE SELECTED_MEMBERSHIP INTO THE SESSION TO BE ABLE TO PAS IT INTO THE NEXT VIEWW
        request.session['selected_membership_type'] = selected_membership.membership_type
        # the above code is passing the value of enterprise or professional into the next veiw
        return HttpResponseRedirect(reverse('memberships:payment'))


@login_required
def PaymentView(request):
    user_membership = get_user_membership(request)
    try:
        selected_membership = get_selected_membership(request)
    except:
        return redirect(reverse("memberships:select_membership"))
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        # try:
        token = request.POST['stripeToken']

        # UPDATE FOR STRIPE API CHANGE 2018-05-21

        '''
        First we need to add the source for the customer
        '''

        customer = stripe.Customer.retrieve(user_membership.stripe_customer_id)
        customer.source = token # 4242424242424242
        customer.save()

        '''
        Now we can create the subscription using only the customer as we don't need to pass their
        credit card source anymore
        '''

        subscription = stripe.Subscription.create(
            customer=user_membership.stripe_customer_id,
            items=[
                { "plan": selected_membership.stripe_plan_id },
            ]
        )
        print(subscription.id)

        return redirect(reverse('memberships:update_transaction',
                                kwargs={
                                    'subscription_id': subscription.id
                                }))

        # except:
        #     messages.info(request, "An error has occurred, investigate it in the console")

    context = {
        'publishKey': publishKey,
        'selected_membership': selected_membership
    }

    return render(request, "memberships/membership_payment.html", context)

@login_required
def UpdateTransactionRecords(request, subscription_id):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    user_membership.membership = selected_membership
    user_membership.save()

    sub, created = Subscription.objects.get_or_create(
        user_membership=user_membership)
    sub.stripe_subscription_id = subscription_id
    sub.active = True
    sub.save()

    try:
        del request.session['selected_membership_type']
    except:
        pass

    messages.info(request, 'Successfully created {} membership'.format(
        selected_membership))
    return redirect(reverse('memberships:select_membership'))

@login_required
def CancelSubscription(request):
    user_sub = get_user_subscription(request)

    if user_sub.active is False:
        messages.info(request, "You dont have an active membership")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    sub = stripe.Subscription.retrieve(user_sub.stripe_subscription_id)
    sub.delete()

    user_sub.active = False
    user_sub.save()

    free_membership = Membership.objects.get(membership_type='Free')
    user_membership = get_user_membership(request)
    user_membership.membership = free_membership
    user_membership.save()
    user = get_object_or_404(User,username=request.username)
    user_email = user.email

    messages.info(
        request, "Successfully cancelled membership. We have sent an email")
    # sending an email here
    send_mail(
        'Subscription successfully cancelled',
        'Successfully cancelled membership. We have sent an email',
        'adebisiayomide68@gmail.com',
        [user_email],
        fail_silently=False,
    )
    
    return redirect(reverse('memberships:select'))
