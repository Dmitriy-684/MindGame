from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
import requests



@csrf_exempt
def user_authorization(request):
    if request.method == "POST":
        body = request.body.decode('utf-8')
        body = json.loads(body)
        Person = User.objects.get(wallet=body["wallet"])
        return HttpResponse("OK")
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")


def post_for_authorization(request):
    url = "http://127.0.0.1:8000/login/"
    wallet = {"wallet": input("Enter your wallet: ")}
    res = requests.post(url, json=wallet)
    if res.status_code == 200:
        return HttpResponse(f"<h4>Данные успешно отправлены {wallet}<h4>")
    else:
        return HttpResponse(f"<h4>Данные не отправлены с кодом {res.status_code}<h4>")
