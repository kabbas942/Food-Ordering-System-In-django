from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def lists(request):
    users = User.objects.all()
    users_dict_list = list(users.values())
    # Assuming 'id' is the primary key of your User model
    users_dict_by_id = dict((user['id'], user) for user in users.values())
    return Response(users_dict_by_id)