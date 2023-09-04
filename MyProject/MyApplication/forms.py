#hanling forms to be displayed to the users.
from django.forms import ModelForm
from .models import *

from django import forms

#here we are importing users model to create customuser.
from django.contrib.auth.models import User

#importing user creation form
from django.contrib.auth.forms import UserCreationForm


#class inheriting from ModelForm
#workers are able to edit from here.
class AddForm(ModelForm):
    #class meta is used to acces something/model and change it in your own way.
    class Meta:
        model = Product
    
        fields = ['recieved_quantity']

#handles how a user will add stock.
class SaleForm(forms.ModelForm):
    class Meta:
        model=Sale
        fields = ['quantity','amount_recieved','issued_to','phone_number','branch_name','sale_date']



    