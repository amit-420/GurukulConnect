from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from main.models import EducatorsData
from django.contrib.auth.models import Group


# GROUP = (
# (None, 'Are you Student or Mentor'),
# ('Mentor', 'Mentor'),
# ('Student', 'Student'),
# )
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email')
    #group = forms.ChoiceField(choices=GROUP)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
       # user.group = self.cleaned_data['group']
        if commit:
            user.save()
        return user

class DatacollectionForm(forms.ModelForm):
    class Meta:
        model = EducatorsData
        fields = "__all__"
