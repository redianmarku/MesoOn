from django.urls import path

from memberships.views import MembershipSelectView,PaymentView,UpdateTransactionRecords,CancelSubscription

app_name = 'memberships'

urlpatterns = [
    path('memberships/', MembershipSelectView.as_view(), name='select_membership'),
    path('payments/', PaymentView, name='payment'),
    path('update_transaction/<subscription_id>/update/', UpdateTransactionRecords, name='update_transaction'),
    path('cancel/', CancelSubscription, name='cancel')

]
