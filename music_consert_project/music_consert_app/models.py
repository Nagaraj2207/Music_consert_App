from django.db import models


class Consert_list(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    available_tickets = models.IntegerField()

class Tickets_Booking(models.Model):
    title = models.CharField(max_length=200)
    ticket_count = models.IntegerField()
    user_name = models.CharField(max_length=100)
    email = models.EmailField()

class Booking_History(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    ticket_count = models.IntegerField()
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_time = models.DateTimeField(auto_now_add=True)  


    