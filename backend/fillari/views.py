from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StationSerializer
from .models import Station

# Create your views here.

def front(request):
    context = { }
    return render(request, "index.html", context)

class StationView(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()