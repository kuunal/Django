from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForms as r1
from .models import Register as r
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        # first_name=request.POST['firstname']        
        # last_name=request.POST['lastname']        
        # email=request.POST['email']        
        # password=request.POST['password']
        # if(r.objects.filter(email=email)):
        #     print("Insidddeeeeeeeeeeeeeeeeee")
        #     messages.warning(request, f'Email already Registered!')
        form = r1(request.POST)
        if not form.is_valid():
            print(form.cleaned_data.get('email'))
            print(form.errors)
            print(form.errors.as_text())
            return render(request ,'register/register.html', {'form':form })
        else:
            # r.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
            new = form.save()
            return redirect('login')    
    else:
        return render(request ,'register/register.html')
        