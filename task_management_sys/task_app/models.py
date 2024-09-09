from django.db import models

class Employee(models.Model):
    empname = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 300)
    role = models.CharField(max_length = 200)

    def __str__(self):
        return self.empname