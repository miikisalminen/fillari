from django.contrib import admin
from .models import Station, Journey

class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')

class JourneyAdmin(admin.ModelAdmin):
    list_display = ('')

admin.site.register(Station, StationAdmin)
admin.site.register(Journey)
