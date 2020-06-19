from django.shortcuts import render
from django.http import JsonResponse
from .models import Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

# Create your views here.
def validate(request):
    if request.method == 'POST':
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        print(user,"SAdSadASDSADASs")
        if user:
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False})
    else:
        form = Login()
        context = {
            "form":form
        }
        return render(request,'login/loginpage.html', context)
