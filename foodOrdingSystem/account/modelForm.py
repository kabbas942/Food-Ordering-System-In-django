from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from account.models import Profile

class AccountForm(UserChangeForm): 
      
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email') #'username',
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            #'username': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-md'}),
        }        
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
        self.fields['password'].required = False
        self.fields['password'].help_text = ''
        
        
        ''' the __init__() method of the AccountForm class is overridden to modify the password field.

By accessing self.fields['password'], we can customize the widget, required status, and help text for the password field. In this case, we set the widget to forms.HiddenInput() to hide the password field, set required to False to make it optional, and set help_text to an empty string to remove the associated message.

Make sure to adjust the fields attribute in the Meta class according to the desired fields you want to include in the form.

Remember to include the necessary imports for forms and User in your code.'''




class extendedAccountForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'zipCode', 'mobileNumber')  
        exclude = ('password1', 'password2')
        widgets = {
            'address' : forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'zipCode': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'mobileNumber': forms.TextInput(attrs={'class': 'form-control form-control-md','type':'number'}),            
            # Add more fields and their corresponding HTML classes
        }   

 
class PasswordChangeForm(SetPasswordForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    #new_password = forms.CharField(widget=forms.PasswordInput)
    #confirm_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(
    label="New Password",
    strip=False,
    widget=forms.PasswordInput,
    error_messages={
            'password_too_short': "Password must be at least 8 characters long.",
            'password_common': "Password can't be a commonly used password.",
            'password_entirely_numeric': "Password can't be entirely numeric.",
        }
    )

    class Meta:
        model = User  # Replace with your User model
        fields = ('password', 'new_password', 'confirm_password')