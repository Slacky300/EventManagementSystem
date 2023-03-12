from django.shortcuts import render, redirect
from . forms import EventPlaceFrm, CreateEventFrm
from . models import Venues, CreatEvent
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


    lct = Venues.objects.all()
    context = {
        'lct' : lct,
    }

    return render(request,'main/places.html',context)

def createEvent(request,slug):

    venue = Venues.objects.get(slug = slug)
    
    ints = {
        'eveManager' : request.user,
        'venue' : venue,
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
                    venueX = Venues.objects.get(id = vnu)
                    venueX.availabililty = False
                    venueX.save()
                    frm.save()
                    messages.success(request,'Submitted Successfully')
                    frm.clean()
                    return redirect('eventCrude')
        except:
            messages.error(request,'Failed to submit')
            return render(request,'main/forms/createEvent.html',context)
    else:
        
        return render(request,'main/forms/createEvent.html',context)
    

def venueDetail(request, slug):

    venue = Venues.objects.get(slug = slug)
    context = {
        'venue' : venue,
    }
    return render(request,'main/details/venueDetail.html',context)



def eventCrude(request):

    events = CreatEvent.objects.filter(eveManager = request.user)
    context = {
        'eve' : events,
    }
    return render(request,'main/crud/eventCrud.html',context)

def eventDelete(request,slug):

    events = CreatEvent.objects.get(slug = slug)
    events.delete()
    messages.success(request,'Event deleted successfully')
    return redirect('eventCrude')

def eventEdit(request, slug):
    event = CreatEvent.objects.get(slug = slug)

    ints = {
        'eveManager' : request.user,
        'venue' : event.venue,
        'name' : event.name,
        'eveTyp' : event.eveTyp,
        'startDate' : event.startDate,
        'endDate' : event.endDate,
        'startTime' : event.startTime,
        'endTime' : event.endTime,
        'nGuest' : event.nGuest,
        'desc' : event.desc,
        'TicketPrice' : event.TicketPrice,

    }
    frm = CreateEventFrm(initial=ints)
    context = {
        'form' : frm,
    }
    if request.method == 'POST':
        try:
            frm = CreateEventFrm(request.POST,request.FILES)
            vnu = request.POST.get('venue')
            if frm.is_valid():
                    venueX = Venues.objects.get(id = vnu)
                    venueX.availabililty = False
                    venueX.save()
                    frm.save()
                    messages.success(request,'Edited Successfully')
                    frm.clean()
                    return render(request,'main/forms/createEvent.html',context)
        except:
            messages.error(request,'Failed to submit')
            return render(request,'main/forms/createEvent.html',context)
    else:
        
        return render(request,'main/forms/createEvent.html',context)


