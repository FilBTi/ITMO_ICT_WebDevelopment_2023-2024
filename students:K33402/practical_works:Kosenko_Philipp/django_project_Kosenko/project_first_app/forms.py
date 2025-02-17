from django import forms
from .models import Car, Driver


class DriverCreateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["username", "password", "first_name", "last_name", "date_of_birth"]
        labels = {
            "username": "Логин",
            "password": "Пароль",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "date_of_birth": "Дата рождения",
            "passport": "Паспорт",
            "address": "Адрес",
            "nationality": "Национальность",
        }


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["number", "brand", "model", "color"]
        labels = {
            "number": "Номер",
            "brand": "Марка",
            "car_model": "Модель",
            "color": "Цвет",
        }


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["number", "brand", "model", "color"]
        labels = {
            "number": "Номер",
            "brand": "Марка",
            "car_model": "Модель",
            "color": "Цвет",
        }
