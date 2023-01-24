from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def openIndexPage(request):
    return render(request,"index.html")

def savestudents(request):
    students=Student()
    students.name=request.POST['name']
    students.phone=request.POST['phone']
    students.section=request.POST['section']
    students.dob=request.POST['dob']
    students.save()
    return redirect("/students-list")

def getAllstudents(request):
    students=Student.objects.all()
    return render(request,"students-list.html",{'students':students})


def openstudents(request):
    return render(request,"students-form.html")

def removestudents(request,id):
    students=Student.objects.get(id=id)
    students.delete()
    return redirect("/student-list")

def editstudent(request,id):
    students=Student.objects.get(id=id)
    return render(request,"students-update-form.html",{'students':students})

def updatestudents(request,id):
    student=Student.objects.get(id=id)
    student.name=request.POST['name']
    student.phone=request.POST['phone']
    student.section=request.POST['section']
    student.dob=request.POST['dob']
    student.save()
    return redirect("/students-list")