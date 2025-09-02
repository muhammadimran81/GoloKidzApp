from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

class ProductFilterForm(forms.Form):
    q = forms.CharField(required=False, label='Search')
    category = forms.CharField(required=False)
    gender = forms.ChoiceField(required=False, choices=[('', 'All'), ('boys','Boys'), ('girls','Girls')])
    size = forms.CharField(required=False)
    price_min = forms.DecimalField(required=False, min_value=0)
    price_max = forms.DecimalField(required=False, min_value=0)