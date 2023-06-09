from django.db import models


# Activity Categories
class ActivityTypes(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


# User activities
class Activities(models.Model):
    name = models.CharField(max_length=255)
    # on_delete=models.SET_NULL in case an activity type gets deleted
    # the activity and user data does not.
    type = models.ForeignKey("ActivityTypes", null=True, on_delete=models.SET_NULL)
    user_description = models.TextField()
    duration = models.IntegerField()
    difficulty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
