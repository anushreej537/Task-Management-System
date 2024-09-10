from django.contrib import admin
from .models import Role,Employee,Project,Task

admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Task)