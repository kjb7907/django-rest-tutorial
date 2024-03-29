from django.db import models
from django.conf import settings

# Create your models here.

class Booking(models.Model):
  subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='bookings')

  date_from = models.DateField()
  date_to = models.DateField(null=True, blank=True)
  room = models.CharField(max_length=100)
  note = models.TextField()

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.subscriber.username + " " + self.room

  class Meta:
    db_table = 'booking'
    ordering = ['-date_from']