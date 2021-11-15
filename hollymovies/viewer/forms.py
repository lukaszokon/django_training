from django.forms import CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea
from django.core.exceptions import ValidationError
from .models import Genre
from datetime import date
import re


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('First letter must be upper')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Past dates only')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(Form):
    title = CharField(max_length=128, validators=[capitalized_validator])
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()
    description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Comedy' and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError("Commedies aren't so good to be rated over 5.")
        return result