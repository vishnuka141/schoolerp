from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from .models import Academic_year
from .forms import AcademicForm
# Create your views here.
def home(request):
    return render(request,'base.html')

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(request,email=email,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid email or password')
            return render(request,'index.html')
    
    return render(request,'index.html')

def signout(request):
    logout(request)
    return redirect('signin')

def academic_year_create(request):
    form = AcademicForm()
    
    qs = Academic_year.objects.all()
    context = {
        'form':form,
        'qs':qs
    }
    if request.method == "POST":
        form = AcademicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academic_year')
    return render(request,'other/academic_year.html',context)


def acdemic_delete(request,pk):
    qs= Academic_year.objects.get(pk=pk)
    qs.delete()
    return redirect('academic_year')
    