from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Events

# Create your views here.

def index(request):
    return render(request, 'ClubApp/index.html')

def getResources(request):
    resources_list=Resource.objects.all()
    context={'resources_list' : resources_list}
    return render(request, 'ClubApp/resources.html' , context=context)

def getMeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'ClubApp/meeting.html', {'meeting_list' : meeting_list})

def meetingDetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    context={
        'meeting' : meeting,
    }
    return render (request, 'ClubApp/meetingdetails.html', context=context)


    