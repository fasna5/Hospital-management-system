from  django.shortcuts import render
from django.http  import HttpResponse

def index(request):
    return  render(request,'index.html')


def about(request):
    return  render(request,'about.html')



def bookings(request):
    return render(request,'bookings.html')



def  doctors(request):
    return render(request,'doctors.html')



def  departments(request):
    return render(request,'departments.html')



def contact(request):
    return render(request,'contact.html')