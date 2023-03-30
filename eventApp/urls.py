from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addEventLocation/',views.addEventL,name='AddEventLct'),
    path('places/',views.places,name='places'),
    path('createEvent/<slug:slug>/',views.createEvent,name='createEvent'),
    path('venue/<slug:slug>/',views.venueDetail,name='venueDetail'),
    path('eventCrud/',views.eventCrude,name='eventCrude'),
    path('eventCrud/<slug:slug>/',views.eventDelete,name='eventDelete'),
    path('crudEdit/<slug:slug>/',views.eventEdit,name='eventEdit'),
    path('login/', views.loginR,name='loginR'),
    path('logout/',views.logoutR,name='logout'),
    path('register/',views.registerR,name='register'),
    path('eventCnfrm/<slug:slug>/',views.confrm,name='EventCnfrm'),
    path('payFor/<slug:slug>/',views.payFor,name='payment'),
    path('payStatus/<slug:slug>/',views.getStatus,name='getIt'),


    path('checkAvial/<slug:slug>/',views.availaibility,name='avail'),
    # path('checkAvial/<slug:slug>/',views.checkAlt,name='avail'),



    path('regClients/<slug:slug>/',views.regClients,name='regClients'),
    path('deletIt/<slug:slug>/',views.sendMsgs,name="deleteIt"),
    path('viewVenues/',views.viewVenues,name='venues'),


    path('stffRegister/',views.stfReg,name='staff'),


    path('activate-user/<uidb64>/<token>',views.activate_user,name='activate'),
    path('checkDate/<slug:slug>/',views.Checkat.as_view(),name='check'),

]