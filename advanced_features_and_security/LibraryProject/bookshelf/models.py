from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view a book"),
            ("can_create", "Can create a book"),
            ("can_edit", "Can edit a book"),
            ("can_delete", "Can delete a book"),
        ]

    class Meta:
        permissions = [
            ("can_view", "Can view a book"),
            ("can_create", "Can create a book"),
            ("can_edit", "Can edit a book"),
            ("can_delete", "Can delete a book"),
        ]

    def __str__(self):
        return self.title
