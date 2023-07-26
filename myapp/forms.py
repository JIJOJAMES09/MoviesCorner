from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Movies


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))



class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=["movie_name","year","runtime","language","genres","poster_image","description"]
        widgets={
            "movie_name":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.NumberInput(attrs={"class":"form-control"}),
            "runtime":forms.TextInput(attrs={"class":"form-control"}),
            "language":forms.TextInput(attrs={"class":"form-control"}),
            "genres":forms.TextInput(attrs={"class":"form-control"}),
            "poster_image":forms.FileInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"})
        }


class MovieChangeForm(forms.ModelForm):

    class Meta:
        model=Movies
        fields=["movie_name","year","runtime","language","genres","poster_image","description"]


class PasswordResetForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1=forms.CharField(label="new password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="confirm new password",widget=forms.PasswordInput(attrs={"class":"form-control"}))