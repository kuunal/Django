from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from register.models import Register as r

# Create your views here.
def validate(request):
    if request.method == 'POST':
        if r.objects.filter(email=request.POST['email']) and r.objects.filter(password=request.POST['password']):
            return JsonResponse({'success':True})
        else:
            return render(request,'login/loginpage.html',{'messages':'Invalid id or pass'})
    else:
        return render(request,'login/loginpage.html')
