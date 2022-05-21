from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Studentmodel,Signupmodels,Employemodel
from .form import StudentForm, UpdateForm,SignupForm,LoginForm, EmployeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def home(request):
    data=Studentmodel.objects.all()
    return render(request, 'home.html', {'data2': data})

def createView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form =StudentForm()
    return render(request, 'create.html', {'form': form})

def edit(request,id):
    data=Studentmodel.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form =UpdateForm(instance=data)
    return render(request, 'edit.html', {'form': form})

def deleteView(request,id):
    data = Studentmodel.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/')

def signupView(request):
    if request.method == 'POST':
        form=SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("user passss=========",username,password)
            user.password = make_password(form.cleaned_data['password'], hasher='default')
            user.save()
            return HttpResponseRedirect('/login')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})


def loginView(request):
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("user pass",username,password)
            user = Signupmodels.objects.get(username=username)
            if check_password(password, user.password):
                messages.success(request, 'Form submission successful')
                print("",messages.success)
                return HttpResponseRedirect("/")
            else:
                form = LoginForm()
                return render(request, 'login.html', {'form': form})
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def employeView(request):
    data =Employemodel.objects.all()
    empfilter=Employemodel.objects.filter(address='Fazilka')
    get_data = Employemodel.objects.values("name")
    query = request.GET.get('q')
    if query:
        results = Employemodel.objects.filter(Q(name=query) | Q(address=query) | Q(qualification=query) ,)
    else:
        results = []
    if request.method =='POST':
        form= EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employecreate')
    else:
        form=EmployeForm()
    return render(request,'employecreate.html',{'form':form, 'data2': data,'empfilter1':empfilter,'getdata1': get_data,'results': results})

# def search(request):
#     query = request.GET.get('q', '')
#     if query or None:
#         # query example
#         results =Employemodel.objects.filter(name=query).distinct()
#     else:
#         results = []
#     return render(request, 'search.html', {'results': results})