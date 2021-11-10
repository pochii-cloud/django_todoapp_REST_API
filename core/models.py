from django.contrib.auth.decorators import login_required
from django.db import models


# Create your models here.

class list(models.Model):
    item = models.CharField(max_length=200, null=False,blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
