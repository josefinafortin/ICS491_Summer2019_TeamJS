from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms

@login_required(login_url="/accounts/login")
def adddevice_view(request):
    if request.method == 'POST':
        form = forms.AddNewDevice(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return render(request, 'adddevice/adddevice.html')
    else:
        form = forms.AddNewDevice()
    return render(request, 'adddevice/adddevice.html', {'form':form})

@login_required(login_url="/accounts/login")
def devices_view(request):
    devices = AddDevice.objects.all()
    return render(request, 'adddevice/adddevice.html', {'devices':devices})
