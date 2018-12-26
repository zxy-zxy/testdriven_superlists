from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class List(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])

    @property
    def name(self):
        return self.item_set.first().text


class Item(models.Model):
    text = models.TextField(blank=False, null=False)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
