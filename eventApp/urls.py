from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addEventLocation/',views.addEventL,name='AddEventLct'),
    path('places/',views.places,name='places'),
    path('createEvent/<slug:slug>/',views.createEvent,name='createEvent'),
    path('venue/<slug:slug>/',views.venueDetail,name='venueDetail'),
]