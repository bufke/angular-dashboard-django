from django.db import models
from django.contrib.auth.models import User


class DashboardStorage(models.Model):
    """ A simple User, key, value storage model """
    user = models.ForeignKey(User)
    key = models.CharField(max_length=2000)
    value = models.TextField(blank=True)

    class Meta:
        unique_together = (('user', 'key'),)
