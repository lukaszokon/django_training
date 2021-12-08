from django.db.transaction import atomic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AdminPasswordChangeForm, UserChangeForm
from django.contrib.auth.models import Group, User
from django.forms import CharField, Textarea, ModelChoiceField

from .models import Profile


class CustomAdminPasswordChangeForm(AdminPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['username', 'first_name', 'groups']

    biography = CharField(label='Your story', widget=Textarea, min_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    @atomic
    def save(self, commit=True):
        user = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile.objects.get(user__pk=user.pk)
        profile.biography = biography
        if commit:
            profile.save()
        return user


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = CharField(label='Your story', widget=Textarea, min_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        user = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=user)
        if commit:
            profile.save()
        return user
