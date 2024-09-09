from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    ROLE_CHOICES = [
        ('Employee','Employee'),
        ('CEO','CEO'),
        ('Team Lead','Team Lead'),
    ]
    role = models.CharField(max_length = 20,choices=ROLE_CHOICES)

    def __str__(self):
        return self.role

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 300)
    role = models.ForeignKey(Role,on_delete = models.CASCADE)
    team_leader = models.ForeignKey('self',null = True, blank = True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.user.username