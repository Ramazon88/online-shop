from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import Karzinka
from django.forms import ModelForm
class UserForm(UserCreationForm):
	class Meta:
		model=User 
		feilds=fields=['username','first_name', 'last_name' , 'password1','password2']	
