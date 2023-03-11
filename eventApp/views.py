from django.shortcuts import render, redirect
from . forms import EventPlaceFrm, CreateEventFrm
from . models import EventPlace, CreatEvent
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
    
    ints = {
        'eveManager' : request.user 
    }
    frm = CreateEventFrm(initial=ints)
    context = {
        'venue' : venue,
        'form' : frm,
    }
    if request.method == 'POST':
        try:
            frm = CreateEventFrm(request.POST,request.FILES)
            vnu = request.POST.get('venue')
            if frm.is_valid():
                    venueX = EventPlace.objects.get(id = vnu)
                    venueX.availabililty = False
                    venueX.save()
                    frm.save()
                    messages.success(request,'Submitted Successfully')
                    frm.clean()
                    return redirect('createEvent')
        except:
            messages.error(request,'Failed to submit')
            return redirect('createEvent')
    else:
        
        return render(request,'main/forms/createEvent.html',context)
    

