from django.shortcuts import render,redirect , get_object_or_404
from student .forms import StudentForm
from student .models import Student
from django.template import loader





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

def detail(request,id):
    detail = Student.objects.get(id=id)
    
    return render(request,'student/detail.html',{'detail':detail})

def delete(request,id):

    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect('list')
    


def update(request, id):                                         
    items = get_object_or_404(Student, id=id)
    form = StudentForm(instance=items)                                                               

    if request.method == "POST":
        form = StudentForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect ('list')
    context = {
        "form":form
    }
    return render(request, 'student/add_student.html', context)

