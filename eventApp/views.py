from django.shortcuts import render, redirect
from . forms import EventPlaceFrm, CreateEventFrm
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . filters import VenueFilter
# Create your views here.
def home(request):
    
    return render(request,'main/land.html')


@login_required(login_url='/login/')
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
    venueFltr = VenueFilter(request.GET, queryset = lct)
    context = {
        'venue' : venueFltr,
    }
    return render(request,'main/places.html',context)


@login_required(login_url='/login/')
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





@login_required(login_url='/login/')
def eventCrude(request):

    events = CreatEvent.objects.filter(eveManager = request.user)
    context = {
        'eve' : events,
    }
    return render(request,'main/crud/eventCrud.html',context)






@login_required(login_url='/login/')
def eventDelete(request,slug):

    events = CreatEvent.objects.get(slug = slug)
    venue = Venues.objects.get(slug = events.venue.slug)
    venue.availabililty = True
    venue.save()
    events.delete()
    messages.success(request,'Event deleted successfully')
    return redirect('eventCrude')






@login_required(login_url='/login/')
def eventEdit(request, slug):
    event = CreatEvent.objects.get(slug = slug)
    venue = Venues.objects.get(slug = event.venue.slug)

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
        'venue' : venue,
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




def loginR(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully')
            return redirect('home')

        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'authentication/login.html')

    else:
        return render(request,'authentication/login.html')


def registerR(request):


    if request.method == 'POST':

        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')

        if UserAccount.objects.filter(email=email).exists():
            messages.warning(request,'User with this email already exists')
            return render(request,'authentication/register.html')
        else:

            myuser = UserAccount.objects.create_user(email, name, password)
            myuser.save()
            messages.success(request,'User Created Successfully')
            return redirect('loginR')

    else:
        return render(request,'authentication/register.html')



def logoutR(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('loginR')



def confrm(request,slug):
    eve = CreatEvent.objects.get(slug = slug)
    eve.status = True
    eve.save()
    messages.success(request,'Ready for payment')
    return redirect('eventCrude')


def payFor(request,slug):

    eventX = CreatEvent.objects.get(slug = slug)
    eventX.payDone = True
    rcpt = Receipt(
        rcptFor = request.user,
        event = eventX,
        status = True
    )
    rcpt.save()
    eventX.save()
    messages.success(request,'Payment Successfull')
    return redirect('eventCrude')

def getStatus(request,slug):

    eventX = CreatEvent.objects.get(slug = slug)
    rcpt = Receipt.objects.get(event = eventX)
    context = {
        'event' : eventX,
        'rcpt' : rcpt,
    }

    return render(request,'main/crud/receipt.html',context)
    