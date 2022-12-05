import json

from django.db.models.manager import BaseManager
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView

from ads.models import Ad, Category



class CategoryListView(ListView):
    model = Category


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):
    def get(self, request) -> JsonResponse:
        categories: BaseManager[Category] = Category.objects.all()
        response = []
        for cat in categories:
            response.append({
                            'id': cat.pk,
                            'name': cat.name,
                            })
        return JsonResponse(response, safe=False)

    def post(self, request) -> JsonResponse:
        data = json.loads(request.body)
        cat: Category = Category.objects.create(**data)
        return JsonResponse({
                            'id': cat.pk,
                            'name': cat.name,
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