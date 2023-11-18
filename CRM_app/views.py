from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForm, addrecord
from .models import Record
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    records = Record.objects.filter(user=request.user)
    #search code
    first_name = request.GET.get('first_name')
    if first_name != '' and first_name is not None:
        records = records.filter(first_name__icontains=first_name)
    
    return render(request, 'CRM_app/home.html',{'records':records})

# Login function
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have login succesfully!')
            return redirect('index')
        else:
            messages.error(request, "We couldn't find an account with that username. Try another, or get a new account.")
            return render(request, 'CRM_app/login.html')
    else:
        return render(request, 'CRM_app/login.html')

# Logout function
def Logout(request):
    logout(request)
    messages.success(request,"You have been logout succesfully")
    return redirect('login')

# Register Function
def Register_user(request):
    form=SignUpForm()
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You have been succesfully Register")
            return redirect('login')
        else:
            messages.success(request,'You have not enter correct data for Registeration!')
            return redirect('Register')
    else:
        form=SignUpForm()
        return render(request,'CRM_app/Register.html',{'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'CRM_app/Record.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'You must have to login to see the data!')
        return redirect('home')

# delete record
def delete_record(request,pk):
    delete_record = Record.objects.get(id=pk, user=request.user)
    delete_record.delete()
    messages.success(request,"Record deleted succesfully!")
    return redirect('index')

# Add record
def add_record(request):
    form = addrecord()

    if request.method == "POST":
        form = addrecord(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user  # Associate the record with the logged-in user
            record.save()
            messages.success(request, 'Record added successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Error adding the record. Please check your input.')

    return render(request, 'CRM_app/addrecord.html', {'form': form})


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = addrecord(request.POST, request.FILES or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated succesfully...')
            return redirect('index')
        return render(request,'CRM_app/update.html',{'form':form})
    else:
        messages.success(request,'You are not enter the Correct Data')
        return redirect('update_record')
    
    
