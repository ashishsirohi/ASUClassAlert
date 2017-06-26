from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    passwd = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

class SignupForm(forms.Form):
    uname = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    passwd1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    passwd2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    pnum = forms.IntegerField(label='Phone', widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}))
