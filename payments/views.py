from django.shortcuts import render,HttpResponse,redirect
from .forms import PaymentTypeForm,PaymentForm
from .models import PaymentType
from django.contrib import messages
# Create your views here.



def payment_type_create(request):
        
    form = PaymentTypeForm()
    plist=PaymentType.objects.all()
    context={
        'plist':plist,
        'form':form
    }
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request,'Already added this payment type')
            return redirect('payment_type')


    return render(request,'payments/payment_type.html',context)

def payment_type_delete(request,pk):
   
    plist = PaymentType.objects.get(pk=pk)
    plist.delete()
    return redirect('payment_type')

def all_payment(request):
    
    return render(request,'payments/all_payments.html')

def add_payment(request):
    form = PaymentForm()
    return render(request,'payments/new_payment.html',{'form':form})