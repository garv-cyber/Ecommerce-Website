from django import forms

class keyboardForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    price = forms.IntegerField(label='Price')
    description = forms.CharField(label='Description', max_length=250)
    image = forms.ImageField(label='Image')

class drumForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    price = forms.IntegerField(label='Price')
    description = forms.CharField(label='Description', max_length=250)
    image = forms.ImageField(label='Image')

class guitarForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    price = forms.IntegerField(label='Price')
    description = forms.CharField(label='Description', max_length=250)
    image = forms.ImageField(label='Image')

class violinForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    price = forms.IntegerField(label='Price')
    description = forms.CharField(label='Description', max_length=250)
    image = forms.ImageField(label='Image')

class feedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    feedback = forms.CharField(label='Your feedback', max_length=300)
    rating_choices = (
        ('1', '⭐'),
        ('2','⭐⭐'),
        ('3','⭐⭐⭐'),
        ('4','⭐⭐⭐⭐'),
        ('5','⭐⭐⭐⭐⭐'),
    )
    rating = forms.ChoiceField(label='rating', widget=forms.Select, choices=rating_choices)