from django import forms
from .models import Studentmodel,Signupmodels, GENDER_CHOICES,Employemodel,STATUS_CHOICES
import logging
from django.contrib.auth import hashers
from django.core.validators import MaxValueValidator, MinValueValidator

# =============================={ CREATE  }=======================================================
YEARS = [x for x in range(1980,2020)]
class StudentForm(forms.ModelForm):
    roll_no=forms.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(10)],required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Please Enter Numbers Only '}))
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    father_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Father Name'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    birth = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=YEARS))
    qualification=forms.CharField(widget=forms.TextInput(attrs={'palceholder': 'Enter Qualifications.'}))
    address=forms.CharField(widget=forms.Textarea(attrs={'palceholder': 'Enter Address'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}))
    img_up =forms.ImageField(widget=forms.FileInput(attrs={'id': 'inp'}),label='')

    class Meta:
        model = Studentmodel
        fields = ('roll_no','name', 'father_name', 'gender','birth', 'qualification', 'address', 'email','img_up',)

# =============================={ UPDATE }=======================================================
class UpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Name"}), max_length=50)
    father_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Father Name"}), max_length=50)
    gender=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Father Name"}), max_length=50)
    birth = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=YEARS))
    qualification = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Qualification"}),max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter Address"})),
    img_up =forms.ImageField(widget=forms.FileInput(attrs={'id': 'inp'}),label='Profile Update')

    class Meta:
        model = Studentmodel
        fields = ('name', 'father_name','gender', 'birth', 'qualification', 'address','img_up',)
# =============================={ SIGN UP }=======================================================
class SignupForm(forms.ModelForm):
        username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                    max_length=30,
                                    label="username",
                                    error_messages={'invalid': (
                                        "This value may contain only letters, numbers and @/./+/-/_ characters.")})
        email = forms.EmailField(label="E-mail")
        password = forms.CharField(widget=forms.PasswordInput,label="Password")
        password2 = forms.CharField(widget=forms.PasswordInput,label="Confirm Password")

        class Meta:
            model = Signupmodels
            fields = ('username', 'email','password',)

        def clean_username(self):
            existing = Signupmodels.objects.filter(username__iexact=self.cleaned_data['username'])
            if existing.exists():
                raise forms.ValidationError("A user with that username already exists.")
            else:
                return self.cleaned_data['username']

        def clean_password2(self):
            password = self.cleaned_data.get("password")
            password2 = self.cleaned_data.get("password2")
            if password and password2 and password != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            return password2


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = Signupmodels
        fields = ('username','password',)

    def clean(self):
        cleanedData = super(LoginForm, self).clean()
        username = cleanedData.get("username")
        try:
            user = Signupmodels.objects.get(username=username)
            if hashers.check_password(cleanedData.get("password"), user.password):
                logging.debug(cleanedData.get("rememberMe"))
            else:
                raise forms.ValidationError("Username or password incorrect")
        except Signupmodels.DoesNotExist:
            raise forms.ValidationError("Username or password incorrect")

class EmployeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Name', 'autocomplete': 'off', 'pattern': '[A-Za-z ]+',
               'title': 'Please Enter Characters Only '}))
    qualification = forms.CharField(max_length=20)
    address = forms.CharField(max_length=250)
    employe_id=forms.IntegerField  (widget=forms.TextInput(attrs={'placeholder': 'Enter Roll No.'}))
    item_select = forms.ChoiceField(choices=STATUS_CHOICES,widget=forms.Select(),label='Select Course')
    class Meta:
        model = Employemodel
        fields = '__all__'
