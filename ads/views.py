from django.http import JsonResponse
from django.shortcuts import render

def root(request):
    return JsonResponse({"status": "ok"})
