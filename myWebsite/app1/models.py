from django.db import models


class UserDataModel(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=40, default=None)
    game_counts = models.IntegerField()
    personal_best = models.IntegerField()

    def __str__(self):
        return self.user_name


class SessionModel(models.Model):
    user_name = models.CharField(max_length=30)
    access_key = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name