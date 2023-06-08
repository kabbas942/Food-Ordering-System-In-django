from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from account.models import Profile

class accountForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password1')
        self.fields.pop('password2')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        #fields = ('username', 'email', 'password1', 'password2')
        
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-md'}),            
            # Add more fields and their corresponding HTML classes
        }

class extendedAccountForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'zipCode', 'mobileNumber')   
        widgets = {
            'address' : forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'zipCode': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'mobileNumber': forms.TextInput(attrs={'class': 'form-control form-control-md','type':'number'}),            
            # Add more fields and their corresponding HTML classes
        }   
        
        


'''class accountForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = '__all__'
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'}),
            'completed' : forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'}),
            # Add more fields and their corresponding HTML classes
        }'''