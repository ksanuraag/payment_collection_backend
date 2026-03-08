from django.db import models

# Create your models here.

class Customer(models.Model):
    EMI_STATUS = (
        ("PENDING", "PENDING"),
        ("PAID", "PAID")
    )
    account_no=models.CharField(max_length=100,unique=True,db_index=True)
    issue_date=models.DateField()
    interest_rate=models.DecimalField(max_digits=6,decimal_places=2)
    tenure = models.IntegerField()
    emi_due= models.DecimalField(max_digits=10, decimal_places=2)
    emi_status = models.CharField(max_length=20, choices=EMI_STATUS, default="PENDING")


    def __str__(self):
        return self.account_no
    
class Payment(models.Model):
    STATUS=(
        ("SUCCESS","SUCCESS"),
        ('FAILED','FAILED')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,db_index=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS)

    def __str__(self):
        return str(self.customer)