from django.shortcuts import render
from django.http import JsonResponse
from .models import Login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def validate(request):
    if request.method == 'POST':
        form = AuthenticationForm( data = request.POST )
        if form.is_valid():
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False})
    else:
        form = Login()
        context = {
            "form":form
        }
        return render(request,'login/loginpage.html', context)
