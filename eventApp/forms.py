from django import forms
from django.forms import ModelForm
from . models import EventPlace, CreatEvent


class DateInput(forms.DateInput):
    input_type = 'date'

class EventPlaceFrm(forms.ModelForm):
    class Meta:
        model = EventPlace
        fields = [
              
              'name',
              'desc',
              'img',
              'cpcty',
              'bkngPrice',
              'areaSpecs',
              'city',
              'address',

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
        }


class CreateEventFrm(forms.ModelForm):
    
    class Meta:
        model = CreatEvent

        fields = [
            'name',
            'desc',
            'startDate',
            'endDate',
            'venue',
            'TicketPrice',
            'img',
        ]

        lables = {

            'name' : 'Enter event name',
            'desc' : 'Event description',
            'startDate' : 'Event start date',
            'endDate' : 'Event end date',
            'venue' : 'Select an event venue',
            'img' : 'Upload an image'

        }

        widgets = {
            'startDate': DateInput(),
            'endDate' :DateInput(),
        }