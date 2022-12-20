from django import forms
from .models import Blog, Contact, Comment
from django.forms.forms import BaseForm
from django.forms.models import ModelForm



banned_email_list = []

class Contact_Form(forms.Form):
    name = forms.CharField(max_length=50, label='Name', required=False)
    surname = forms.CharField(max_length=50, label='Surname', required=False)
    email = forms.EmailField(max_length=50, label='Email', required=True)
    email2 = forms.EmailField(max_length=50, label='Email Kontrol', required=True)
    content = forms.CharField(max_length=1000, label='Content', required=True)

    def __init__(self, *args, **kwargs):
        super(Contact_Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Işıl':
            raise forms.ValidationError('Please enter a name but Işıl')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in banned_email_list:
            raise forms.ValidationError('This email has been banned')
        return email

    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("Emails don't match")




class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category_choices', 'image', 'link']

    def __init__(self, *args, **kwargs):
        super(Blog_Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})


class PostQuery_Form(forms.Form):
    CATEGORY_CHOICES = ((None, 'Please Select a Category'), ('all','ALL'), ('art', 'ART'), ('science', 'SCIENCE'), ('sports', 'SPORTS'), ('photography', 'PHOTOGRAPHY'),
                        ('technology', 'TECHNOLOGY'), ('travel', 'TRAVEL'), ('other', 'OTHER'))
    search = forms.CharField(label='Search', max_length=500, widget=forms.TextInput(attrs={'placeholder':'Search for anything', 'class': 'form-control'}),
                             required=False)
    search_category = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control'}), choices=CATEGORY_CHOICES, required=False)


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'surname', 'email', 'content']

    def __init__(self, *args, **kwargs):
        super(Comment_Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


