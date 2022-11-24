from django.shortcuts import render,redirect
from student .forms import StudentForm
from student .models import Student


# Create your views here.
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('list')
        
        

    form = StudentForm()
    return render(request,'student/add_student.html',{'form':form})

def sutdent_list(request):
    students = Student.objects.all()

    return render(request,'student/studentlist.html',{'students':students})

def detail(request):
    return render(request,'student/detail.html')

