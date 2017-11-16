import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

app_id = 1552973814793221
app_secret = 'ef94d617261d205dbc09d9d9d50f519a'


def index(request):
    context = {
        "app_id": app_id,
    }
    return render(request, 'login.html', context)


def login(request):
    code = request.GET['code']
    redirect_uri = f"{request.scheme}://{request.META['HTTP_HOST']}{reverse('login')}"
    url_access_token = "https://graph.facebook.com/v2.11/oauth/access_token"

    params_access_token = {
        "client_id": app_id,
        "redirect_uri": redirect_uri,
        "client_secret": app_secret,
        "code": code,
    }

    response = requests.get(url_access_token, params=params_access_token)
    url_debug_token = 'https://graph.facebook.com/debug_token'
    access_token = response.json()['access_token']
    params_debug_token = {
        "input_token":  access_token,
        "access_token": f'{app_id}|{app_secret}'
    }

    url_user_info = 'https://graph.facebook.com/me'
    user_info_fields = [
        'id',
        'first_name',
        'last_name',
        'picture',
        'email',
    ]
    params_user_info = {
        "fields": ','.join(user_info_fields),
        "access_token": access_token
    }
    user_info = requests.get(url_user_info, params=params_user_info)

    return HttpResponse(user_info.json().items())
