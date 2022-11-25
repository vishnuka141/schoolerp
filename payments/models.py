from django.db import models
from student.models import Student
from main.models import Academic_year
# Create your models here.
class PaymentType(models.Model):
   
    fee_type = models.CharField(max_length=50,unique=True)

    def __str__(self) -> str:
        return self.fee_type

class Payment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    academic_year = models.ForeignKey(Academic_year,on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("closed", "Closed")],
        default="active",
    )
    payment_type = models.ForeignKey(PaymentType,on_delete=models.CASCADE)

   
class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.IntegerField()