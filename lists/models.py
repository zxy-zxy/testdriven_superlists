from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class List(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='got_shared')

    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])

    @property
    def name(self):
        return self.item_set.first().text

    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=list_)
        return list_


class Item(models.Model):
    text = models.TextField(blank=False, null=False)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
