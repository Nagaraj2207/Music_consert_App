from django.contrib import admin
from .models import Consert_list,Tickets_Booking

# Register your models here.

admin.site.register(Tickets_Booking)

class CONSERTLIST(admin.ModelAdmin):
    list_display =["title","description","venue","date","artist","available_tickets"]
    list_display_links =["title","description","venue","date","artist","available_tickets"]
    list_filter = ["title"]
    search_fields = ["title"]

admin.site.register(Consert_list,CONSERTLIST)