from django import forms
from django.forms import ModelForm
from . models import Venues, CreatEvent


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventPlaceFrm(forms.ModelForm):
    class Meta:
        model = Venues
        fields = [
              
              'name',
              'desc',
              'img',
              'cpcty',
              'speciality',
              'bkngPrice',
              'mobNo',
              'areaSpecs',
              'city',
              'address',
              'owner',
              

        ]
        labels = {
            'name' : 'Name',
            'desc' : 'Description about the place',
            'img' : 'Upload Image',
            'cpcty' : 'Capacity of the place',
            'bkngPrice' : 'Price of Booking',
            'areaSpecs' : 'Specifications of the area',
            'city' : 'City',
            'address': 'Address',
            'mobNo' : 'Mobile no.',
            'speciality' : 'Speciality',
            'owner' : '',
            
        }


class CreateEventFrm(forms.ModelForm):
    
    class Meta:
        model = CreatEvent

        fields = [
            'name',
            'eveTyp',
            'startDate',
            'endDate',
            'startTime',
            'endTime',
            'venue',
            'nGuest',
            'tBkngPrice',
            'TicketPrice',
            'img',
            'eveManager',
            'desc',
        ]

        labels = {

            'name' : 'Enter event name',
            'eve'  : 'Event type',
            'desc' : 'Event description',
            'startDate' : 'Event start date',
            'endDate' : 'Event end date',
            'nGuest' : 'Number of guests',
            'venue' : 'Select an event venue',
            'img' : 'Upload an image',
            'eveManager' : '',
            'startTime' : 'Time of event',
            'endTime' : 'Time the event will end',
            'tBkngPrice' : 'Total Booking Price',

        }

        widgets = {
            'startDate': DateInput(),
            'endDate' :DateInput(),
            'startTime' : TimeInput(),
            'endTime' : TimeInput(),
        }