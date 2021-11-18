from django.db import models
from django.db.models import CharField, Model, DO_NOTHING, DateField, DateTimeField, ForeignKey, IntegerField, \
    TextField, FloatField, SlugField
from django.utils.text import slugify


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = FloatField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Create your models here.
