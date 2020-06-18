from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.register_user, name="register")
]