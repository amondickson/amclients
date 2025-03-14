from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

# Home page
def home(request):
    return render(request, 'webapp/index.html')

# Register a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account creation successful!🤝")
            return redirect("my-login")
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)

# Login a user
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)

# Dashboard
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.filter(creator=request.user)
    context = {'records': my_records}
    return render(request, 'webapp/dashboard.html', context=context)

# Update a record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = get_object_or_404(Record, id=pk, creator=request.user)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record update successful!👍")
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)

# Read/view a singular record
@login_required(login_url='my-login')
def singular_record(request, pk):
    record = get_object_or_404(Record, id=pk, creator=request.user)
    context = {'record': record}
    return render(request, 'webapp/view-record.html', context=context)

# Delete a record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = get_object_or_404(Record, id=pk, creator=request.user)
    record.delete()
    messages.success(request, "Record deletion successful!🚮")
    return redirect("dashboard")

# User logout
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out 🔐")
    return redirect("my-login")

# Create a record
@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.creator = request.user
            record.save()
            messages.success(request, "Record creation successful!😎")
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)
