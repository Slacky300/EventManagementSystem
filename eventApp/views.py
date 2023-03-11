from django.shortcuts import render, redirect
from . forms import EventPlaceFrm, CreateEventFrm
from . models import EventPlace
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'main/land.html')

def addEventL(request):

    frm = EventPlaceFrm()
    context = {
        'form' : frm
    }
    if request.method == 'POST':
        try:

            frm = EventPlaceFrm(request.POST,request.FILES)
            if frm.is_valid():
                frm.save()
                messages.success(request,'Submitted Successfully')
                return redirect('AddEventLct')
        except:
            messages.error(request,'Failed to submit')

    return render(request,'main/forms/addEventLocation.html',context)

def places(request):


    lct = EventPlace.objects.all()
    context = {
        'lct' : lct,
    }

    return render(request,'main/places.html',context)

def createEvent(request):

    venue = EventPlace.objects.all()
    frm = CreateEventFrm()
    context = {
        'venue' : venue,
        'form' : frm,
    }
    if request.method == 'POST':
        try:
            frm = CreateEventFrm(request.POST,request.FILES)
            if frm.is_valid():
                    frm.save()
                    messages.success(request,'Submitted Successfully')
                    return redirect('AddEventLct')
        except:
            messages.error(request,'Failed to submit')
    else:
        
        return render(request,'main/forms/createEvent.html',context)