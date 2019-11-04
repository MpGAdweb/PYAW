from django import forms

class ContactForm(forms.Form):
    from_name = forms.CharField(label='Nome', required=True)
    from_email = forms.EmailField(label='E-mail',required=True)
    message = forms.CharField(label='Mensagem',widget=forms.Textarea(attrs={'rows': 5}), required=True)
    newslleter = forms.BooleanField(required=False, initial=True, label='Sim, quero receber a newsletter!')
class AuditForm(forms.Form):
    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='Email', required=True)
    url = forms.URLField(label='URL',initial='http://')
class FormContact(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Tel')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'rows': 5}))
