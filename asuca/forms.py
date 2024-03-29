from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter Username'}))
    passwd = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control input-md', 'placeholder':'Enter Password'}))

class SignupForm(forms.Form):
    uname = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter Email'}))
    passwd1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter Password'}))
    passwd2 = forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control input-md', 'placeholder': 'Re-Enter Password'}))
    pnum = forms.IntegerField(label='Phone', widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter Phone Number'}))

class SearchForm(forms.Form):
    courseid = forms.CharField(label='Course Id', widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter 5 digit Course Id e.g. 80304'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter subject name e.g. CSE'}))
    subj_num = forms.CharField(label='Number', widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder': 'Enter Course Number e.g. 591'}))