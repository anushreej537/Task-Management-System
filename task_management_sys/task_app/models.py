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


class Project(models.Model):
    project_name = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null= True,blank=True)

    def __str__(self):
        return self.project_name


    
class Task(models.Model):
    STATUS_CHOICES = [
    ('Process', 'Process'),
    ('Pending', 'Pending'),
    ('Complete', 'Complete'),
    ('Testing', 'Testing'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks') # TL who assigns
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks') # Employee working on the task
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.project}"