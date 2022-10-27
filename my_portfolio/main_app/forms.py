from django.forms import ModelForm
from .models import Contact, Review

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','phone','buisness','title']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['stars' , 'alias' , 'comment']