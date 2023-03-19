from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(City)
admin.site.register(Venues)
admin.site.register(CreatEvent)
admin.site.register(Receipt)
admin.site.register(Msgs)