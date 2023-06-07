from django.contrib.auth.models import User

def profileData(request):
    # Retrieve the data you want to send to the base.html template
    # You can perform any necessary calculations or queries here
    
    
    if request.user.is_authenticated:
        userId = User.objects.get(id=request.user.id)
        custom_data = {
        'userName':userId.username,        
        # Add more key-value pairs as needed
        }
        return custom_data
    return {}
'''
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>{{ my_variable }}</h1>
    <ul>
        {% for item in my_list %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>'''
