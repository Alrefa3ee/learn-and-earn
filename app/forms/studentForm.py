from django import forms
from app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'username','password', 'age' ,'gread')