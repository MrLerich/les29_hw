import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def first(request) -> JsonResponse:
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdListCreateView(View):
    def get(self, request) -> JsonResponse:
        ads = Ad.objects.all()
        response: list = []
        for ad in ads:
            response.append({
                'id': ad.pk,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
            })
        return JsonResponse(response, safe=False)

    def post(self, request) -> JsonResponse:
        data = json.loads(request.body)
        ad = Ad.objects.create(**data)
        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
        },
            safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):
    def get(self, request) -> JsonResponse:
        categories = Category.objects.all()
        response = []
        for cat in categories:
            response.append({
                            'id': cat.pk,
                            'name': cat.name,
                            })
        return JsonResponse(response, safe=False)

    def post(self, request) -> JsonResponse:
        data = json.loads(request.body)
        cat = Category.objects.create(**data)
        return JsonResponse({
                            'id': cat.pk,
                            'name': cat.name,
                            },
                            safe=False)


class AdDetailView(DetailView):
    queryset = Ad.objects.all() #запрос в базу

    def get(self, request, *args, **kwargs) -> JsonResponse:
        ad = self.get_object()
        return JsonResponse({
                            'id': ad.pk,
                            'name': ad.name,
                            'price': ad.price,
                            'description': ad.description,
                            'address': ad.address,
                            'is_published': ad.is_published
                            },
                            safe=False)


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs) -> JsonResponse:
        cat = self.get_object()
        return JsonResponse({
                            'id': cat.pk,
                            'name': cat.name,
                            },
                            safe=False)