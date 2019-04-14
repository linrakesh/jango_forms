from django import forms

class ContactUs(forms.Form):
    name =     forms.CharField(label='Your Name', max_length=30, required=True)
    email =    forms.EmailField(label='Your Email', max_length=100,required=True)
    message =  forms.CharField(label='Your Message', max_length=1000, required=False,widget=forms.Textarea)