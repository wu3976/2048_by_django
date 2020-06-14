from django import forms


class LoginForm(forms.Form):

    userName = forms.CharField(label="Username:", max_length=20, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "input_field",
        'id': "userName",
        'name': "userName"
    }))
    passWord = forms.CharField(label="Password  ", max_length=20, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': "input_field",
        'id': "passWord",
        'name': "passWord"
    }))


class SignupForm(forms.Form):

    userName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "input_field",
        'id': "userName_s",
        'name': "userName"
    }))
    passWord = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': "input_field",
        'id': "passWord_s",
        'name': "passWord"
    }))
    email = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'input_field',
        'id': 'email',
        'name': "email"
    }))