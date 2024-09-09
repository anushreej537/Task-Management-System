from django.db import models

class Role(models.Model):
    ROLE_CHOICES = [
        ('Employee','Employee'),
        ('CEO','CEO'),
        ('Team Lead','Team Lead'),
    ]

    role = models.CharField(max_length=20,choices=ROLE_CHOICES)

    def __str__(self):
        return self.role
    
class Employee(models.Model):
    empname = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)

    def __str__(self):
        return self.empname
    
    
