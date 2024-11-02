from  django.shortcuts import render
from django.http  import HttpResponse
from . models import Departments,Doctors

def index(request):
    return  render(request,'index.html')


def about(request):
    return  render(request,'about.html')



def bookings(request):
    return render(request,'bookings.html')




def  doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)




def  departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)

def contact(request):
    return render(request,'contact.html')