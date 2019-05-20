from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Events
from .forms import ResourceForm

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

def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()

    else: 
            form=ResourceForm()
    return render(request, 'ClubApp/newresource.html', {'form' : form})

    