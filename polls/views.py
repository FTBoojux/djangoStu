import random

from django import shortcuts
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from djangoStu.model.UserInfo import UserInfo


# Create your views here.
def index(request):
    random_num = random.randint(1, 100)
    return HttpResponse(f"Random number: {random_num}.")


def list_user(request):
    users = UserInfo.objects.all()
    user_list = []
    for user in users:
        user_list.append({
            'id': user.uid,
            'name': user.username,

        })
    return JsonResponse({'users': user_list})


def get_user_by_id(request, id: int):
    user = shortcuts.get_object_or_404(UserInfo, pk=id)
    return JsonResponse(user.to_dict())
