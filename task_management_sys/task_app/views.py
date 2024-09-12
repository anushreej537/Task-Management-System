from django.shortcuts import render,redirect
from .models import Role,Employee,Project,Task
from django.contrib import messages

def home(request):
    emp_obj = Employee.objects.all()
    return render(request,'home.html',{'emp_obj':emp_obj})


def addemp(request):
    role_obj = Role.objects.all()
    print(role_obj)
    return render(request,'addemployee.html',{'role_obj':role_obj})

def employee(request):
    if request.method == 'POST':
        empname = request.POST['empname']
        email = request.POST['email']
        role_id = request.POST['role']
        role = Role.objects.get(id=role_id)
        print(empname)
        print(email)
        print(role)
        
        if Employee.objects.filter(email = email).exists():
            messages.error(request,'email already exist')
            return redirect(request,'/home/')
        else:
            Employee.objects.create(empname=empname, email=email, role=role)
            return render(request,'add.html')


def project(request):
    return render(request,'project.html')


def addproject(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        Project.objects.create(project_name=project_name, description=description, start_date=start_date , end_date=end_date)

    else:
        return redirect('/project/')
