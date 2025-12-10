from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_publicate']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите фото'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите категорию'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Назначьте цену'
        })

        self.fields['is_publicate'].widget.attrs.update({
            'class': 'form-check-input'
        })

    def clean_description(self):
        description = self.cleaned_data.get('description')
        incorrect_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if [word for word in incorrect_words if word in description]:
            raise ValidationError("В описании присутствует запрещенное слово")
        return description

    def clean_name(self):
        name = self.cleaned_data.get('name')
        incorrect_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if [word for word in incorrect_words if word in name]:
            raise ValidationError("В названии присутствует запрещенное слово")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Цена не может быть 0 или отрицательной")
        return price
