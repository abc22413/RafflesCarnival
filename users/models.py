from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Role constants
    TREASURER = "TR"
    MANAGER = "MR"
    ADMIN = "AM"
    TICKET_ADMIN = "SU"
    ROLE_CHOICES = (
        (TREASURER, "Treasurer"),
        (MANAGER, "Manager"),
        (ADMIN, "Admin"),
        (TICKET_ADMIN, "Ticket Admin")
    )
    role = models.CharField(
        max_length = 2,
        choices = ROLE_CHOICES,
        default = TREASURER
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()