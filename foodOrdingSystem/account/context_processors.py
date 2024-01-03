from django.contrib.auth.models import User

def profileData(request):
    # Retrieve the data you want to send to the base.html template
    # You can perform any necessary calculations or queries here
    
    
    if request.user.is_authenticated:
        userId = User.objects.get(id=request.user.id)
        if userId.last_name:
            name = userId.last_name
        else:
            name= "User"
        custom_data = {
        'userName':name,        
        # Add more key-value pairs as needed
        }
        return custom_data
    return {}