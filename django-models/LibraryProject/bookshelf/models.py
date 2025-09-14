from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_create", "Can create a book"),
            ("can_delete", "Can delete a book"),
        ]

    def __str__(self):
        return self.title
