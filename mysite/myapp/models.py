from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
STATUS_CHOICES = (
    ('"--Select--"',"--Select--"),
    ("Java",'Java'),
    ("Python",'Python'),
    ("Web Desining",'Web Desining'),
    ("PHP",'PHP')
)
class Studentmodel(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    birth=models.DateField()
    qualification=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    email=models.EmailField(max_length=250)
    img_up = models.ImageField(upload_to='pictures/',null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name




class Signupmodels(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Employemodel(models.Model):
    employe_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    qualification = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    item_select=models.CharField(max_length=50,choices=STATUS_CHOICES,default="dsjf")

    def __str__(self):
        return self.name
