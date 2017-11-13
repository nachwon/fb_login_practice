import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

app_id = 1552973814793221
app_secret = 'bb9f21234cde9c81be4df7c13f6f82b9'


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
    result = response.json()

    return HttpResponse(result.items())
