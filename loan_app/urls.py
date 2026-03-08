from django.urls import path,include
from loan_app import views

urlpatterns = [
    path('customer/',views.customer_details),
    path('payments/',views.make_payment),
    path('payments/<str:account_no>/',views.payment_history)
]
