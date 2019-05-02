from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Events

# Create your views here.

def index(request):
    return render(request, 'ClubApp/index.html')

def getResources(request):
    resources_list=Resource.objects.all()
    context={'resources_list' : resources_list}
    return render(request, 'ClubApp/resources.html' , context=context)
    