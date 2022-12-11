from django import forms



banned_email_list = ['isilbalki@gmail.com']


class Contact_Form(forms.Form):
    name = forms.CharField(max_length=50, label='Name', required=False)
    surname = forms.CharField(max_length=50, label='Surname', required=False)
    email = forms.EmailField(max_length=50, label='Email', required=True)
    email2 = forms.EmailField(max_length=50, label='Email Kontrol', required=True)
    content = forms.CharField(max_length=1000, label='Content', required=True)

    def __int__(self, *args, **kwargs):
        super(Contact_Form, self).__int__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

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