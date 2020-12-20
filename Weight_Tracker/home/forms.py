from django import forms
from django.http import request

from .models import Person, Bmi, ConsumeFoodDetail, FoodDetail


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         # fields = [
#         #     'profile'
#         # ]
#         exclude = ['username', 'email', 'firstname', 'lastname',
#                    'gender',
#                    'age',
#                    'date_of_birth',
#                    'current_weight',
#                    'targeted_weight',
#                    'height',
#                    'time_period',
#                    'password',
#                    'usertype'
#                    ]


class BmiForm(forms.ModelForm):
    height = forms.FloatField(label='Height', widget=forms.TextInput(attrs={"placeholder": "Enter your height in ft"}))
    weight = forms.FloatField(label='Weight', widget=forms.TextInput(attrs={"placeholder": "Enter your weight in kg"}))

    class Meta:
        model = Bmi
        fields = [
            'height',
            'weight'
        ]


class AddConsumeFood(forms.ModelForm):
    # username = forms.FloatField(label='Height', widget=forms.TextInput(attrs={"placeholder": "Enter Username"}))
    class Meta:
        model = ConsumeFoodDetail
        fields = [
            'username',
            'food_name',
            'gram',
            'category',
            'date'
        ]


class FoodDetailForm(forms.ModelForm):
    class Meta:
        model = FoodDetail
        fields = [
            'food_name',
            'cal',
            'fat',
            'protein',
            'carbs',
            'category'
        ]
