from django.db import models
from main.models import Academic_year

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other','other'),
    )
    status_choice = (
        ('Active', 'active'),
        ('Closed', 'closed'),
    )
    batch_choices = (
        ('LKG','lkg'),
        ('UKG', 'ukg'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    birth_certificate = models.ImageField(upload_to='DOB',null=True,blank=True)
    
    admission_number = models.IntegerField(unique=True)
    academic_year = models.ForeignKey('main.Academic_year', on_delete=models.CASCADE)
   
  
    parent_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=10, choices=status_choice,default='Active')
    batch =  models.CharField(max_length=10, choices=batch_choices)

    def __str__(self):
        return self.full_name




class Students(models.Model):

    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other','other'),
    )
    status_choice = (
        ('Active', 'active'),
        ('Closed', 'closed'),
    )
    batch_choices = (
        ('LKG','lkg'),
        ('UKG', 'ukg'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    birth_certificate = models.ImageField(upload_to='DOB',null=True,blank=True)
    
    admission_number = models.IntegerField(unique=True)
  
    parent_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=10, choices=status_choice,default='Active')
    batch =  models.CharField(max_length=10, choices=batch_choices)

    def __str__(self):
        return self.full_name
    academic_year = models.ForeignKey('main.Academic_year', on_delete=models.CASCADE)
   
