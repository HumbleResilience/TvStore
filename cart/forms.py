from django import forms


PRODUCT_QUANITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class CartAddProductForm(forms.Form):
    quanity = forms.TypedChoiceField(choices=PRODUCT_QUANITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    