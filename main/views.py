from django.shortcuts import render
from django.views import View
from api.models import *

# Create your views here.
def login(request):
    return render(request, 'login.html')

class LocationViewSet(View):
    def get(self, request):
        locations = Location.objects.all().order_by('date_modified')
        context = {
            'locations': locations
        }
        return render(request, 'dashboard.html')