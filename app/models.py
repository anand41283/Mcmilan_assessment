from django.db import models

# Create your models here.
class Department(models.Model):
    department=models.CharField(max_length=300)

    def __str__(self):
        return self.department
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    reg_number=models.IntegerField(unique=True)
    phone_number=models.IntegerField()
    email=models.EmailField()
    depart=models.ForeignKey(Department,on_delete=models.CASCADE)