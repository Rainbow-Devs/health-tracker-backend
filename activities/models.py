from django.db import models
from django.contrib.auth.models import User


# Activity Categories
class ActivityName(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


# User activities
class Activity(models.Model):
    # on_delete=models.CASCADE in case a user gets deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # on_delete=models.SET_NULL in case an activity type gets deleted
    # the activity and user data does not.
    activity_name = models.OneToOneField(
        ActivityName, on_delete=models.SET_NULL, null=True
    )
    user_description = models.TextField(max_length=255)
    duration = models.IntegerField()
    difficulty = models.IntegerField()
    start_time = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
