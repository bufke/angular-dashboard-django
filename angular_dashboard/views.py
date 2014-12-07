from django.http import HttpResponse
from django.views.generic import View
from .models import DashboardStorage
import json


class StorageView(View):
    def get_storage(self, request, key):
        return DashboardStorage.objects.get_or_create(
            user=request.user, key=key)[0]

    def get(self, request, key):
        storage = self.get_storage(request, key)
        return HttpResponse(storage.value)

    def post(self, request, key):
        storage = self.get_storage(request, key)
        storage.value = json.loads(request.body.decode('UTF-8'))['value']
        storage.save()
        return HttpResponse('')

    def delete(self, request, key):
        storage = self.get_storage(request, key)
        storage.delete()
        return HttpResponse('')
