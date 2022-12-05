import json

from django.db.models.manager import BaseManager
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
        ad: Ad = Ad.objects.create(**data)
        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
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


