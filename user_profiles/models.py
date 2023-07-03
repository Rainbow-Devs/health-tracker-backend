from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Pronouns(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, null=True)
    # pronouns = models.ForeignKey("Pronouns", null=True, on_delete=models.SET_NULL)
    short_term_goal = models.TextField(max_length=255)
    long_term_goal = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created and not UserProfile.objects.filter(user=instance).exists():
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    if instance.userprofile.display_name is None:
        instance.userprofile.display_name = (
            f"{instance.first_name} {instance.last_name}"
        )
    instance.userprofile.save()
