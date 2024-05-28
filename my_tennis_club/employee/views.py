from django.shortcuts import render
from .forms import EmployeeForm
import requests
from bs4 import BeautifulSoup as bs
# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def employee(request):
    if request.method=='POST':
        data =request.POST
        email=data['email']
        pawd=data['password'] 
        Details={
                'Email':email,
                'Password':pawd,  
        }
    else:
        Details={
            'Email':'No email',
            'Password':'No password '
        }
    return render(request,"employee/index.html",Details)
def features(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        print(form.is_valid())
        print(form.cleaned_data)
    form=EmployeeForm()
    context={
        'form':form
    }
    return render(request,'features/index.html',context)

def project(request):
    if request.method=='POST':
        data=request.POST
        word=data['word']
        payload = {'q':word}
        r = requests.get('https://xdee.pythonanywhere.com/meaning/',params=payload).text
        soup=bs(r,'lxml')
        print(soup)
       

    return render(request,'project/project1.html')