from django.http import JsonResponse


def first(request):
    return JsonResponse({"status": "ok"})
