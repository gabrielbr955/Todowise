from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class List(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} (done={self.done})'
