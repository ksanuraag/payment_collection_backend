from django.shortcuts import render

# Create your views here.
from .serializer import CustomerSerializer,PaymentSerializer
from .models import Customer,Payment
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def customer_details(request):
    customer=Customer.objects.all()
    serializer=CustomerSerializer(customer,many=True)

    return Response({'message':"customer fetched successfully",'data':serializer.data})


@csrf_exempt
@api_view(['POST'])
def make_payment(request):
    account_no = request.data.get("account_no")
    amount = request.data.get("amount")
    if not account_no:
        return Response({"error":"account no is required"},status=status.HTTP_400_BAD_REQUEST)
    if not amount:
        return Response({"error":"amount is required"},status=status.HTTP_400_BAD_REQUEST)
    
    try:
        amount = Decimal(amount)
    except:
        return Response({'error':'invalid amount'},status=status.HTTP_400_BAD_REQUEST)

    try:
        customer = Customer.objects.get(account_no=account_no)
    except Customer.DoesNotExist:
        return Response({"error": "customer with this account number doesn't exist"},status=status.HTTP_404_NOT_FOUND)
    if amount != customer.emi_due:
        return Response({"error": "Amount must match EMI due"}, status=400)
    if customer.tenure == 0:
        return Response({"error": "Loan already completed"}, status=400)
    if amount <= 0:
        return Response({"error": "Amount must be greater than 0"},status=status.HTTP_400_BAD_REQUEST)
    if amount ==customer.emi_due:
        payment = Payment.objects.create(customer=customer,payment_amount=amount,status="SUCCESS")
        # Update paid amount
        customer.total_paid_amount += amount

        # Reduce tenure
        customer.tenure -= 1

        # Check if loan finished
        if customer.total_paid_amount >= customer.total_loan_amount:
            customer.emi_status = "PAID"
        customer.save()
        serializer = PaymentSerializer(payment)
    else:
        return Response({'error':'amount cannot and emi amount doesnt match'},status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Payment successful","data": serializer.data})

@csrf_exempt
@api_view(['GET'])
def payment_history(request, account_no):
    try:
        customer=Customer.objects.get(account_no=account_no)
    except Customer.DoesNotExist:
        return Response({'error':'customer not found'},status=status.HTTP_404_NOT_FOUND)
    payments = Payment.objects.filter(customer=customer)
    serializer = PaymentSerializer(payments, many=True)
    return Response({'message':'payment history fetched','data':serializer.data})