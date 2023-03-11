from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addEventLocation/',views.addEventL,name='AddEventLct'),
    path('places/',views.places,name='places'),
    path('createEvent/',views.createEvent,name='createEvent')
]