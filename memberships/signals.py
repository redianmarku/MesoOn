# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from memberships.models import UserMembership
# from django.conf import settings
#
# import stripe
# stripe.api_key = settings.STRIPE_SECRET_KEY
#
#
# @receiver(post_save,sender=User)
# def create_user_membership(sender,instance,created,*args,**kwargs):
#     if created:
#         UserMembership.objects.get_or_create(user=instance)
#     user_membership,created = UserMembership.objects.get_or_create(user=instance)
#     if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id = '':
#         new_customer_id = stripe.Customer.create(email=instance.email)
#         user_membership.stripe_customer_id = new_customer_id['id']
#         # user_membership.save();
#
# @receiver(post_save,sender=User)
# def save_user_membership(sender,instance,*args,**kwargs):
#     instance.UserMembership.save()
