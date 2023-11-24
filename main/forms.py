from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import *


class ProductForm(ModelForm):
    name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'type': 'text',
                                                                        'id': 'name',
                                                                        'name': 'name',
                                                                        'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
    anons = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name',
                                                                          'name': 'name',
                                                                          'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
                                                            'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                                                            'id': 'file_input',
                                                            'type': 'file'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                                             'id': 'name',
                                                             'name': 'name',
                                                             'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))

    # cat = forms.ChoiceField(widget=forms.ChoiceField(attrs={'id':'category'}))
    class Meta:
        model = Product
        fields = ('name', 'anons', 'status', 'image', 'price', 'cat')






class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                                                            'id': 'username',
                                                                            'type': 'text',
                                                                            'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                                            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                                                            'id': 'password',
                                                                            'type': 'text',
                                                                            'placeholder': 'Password'}))



class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={''
                                                             'class': 'peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0',
                                                             'type': 'text',
                                                             'placeholder': 'Email address',
                                                             'id': 'for exampleFormControlInput2'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={''
                                                             'class': 'peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0',
                                                             'type': 'password',
                                                             'placeholder': '********',
                                                             'id': 'exampleFormControlInput22'}))
class RegisterForm(UserCreationForm):
    email = forms.EmailField()



class ProductChangeForm(ModelForm):
    name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'type': 'text',
                                                                        'id': 'name',
                                                                        'name': 'name',
                                                                        'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
    anons = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name',
                                                                          'name': 'name',
                                                                          'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
                                                            'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                                                            'id': 'file_input',
                                                            'type': 'file'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                                             'id': 'name',
                                                             'name': 'name',
                                                             'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))

    # cat = forms.ChoiceField(widget=forms.ChoiceField(attrs={'id':'category'}))
    class Meta:
        model = Product
        fields = ('name', 'anons', 'status', 'image', 'price', 'cat')

