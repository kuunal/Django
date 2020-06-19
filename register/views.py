from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForms
from .models import Register as r
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']        
        last_name=request.POST['lastname']        
        email=request.POST['email']        
        password=request.POST['password']
        if(r.objects.filter(email=email)):
            print("Insidddeeeeeeeeeeeeeeeeee")
            messages.warning(request, f'Email already Registered!')
            return render(request ,'register/register.html')
        else:
            r.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
            return redirect('login')
    else:
        return render(request ,'register/register.html')
        