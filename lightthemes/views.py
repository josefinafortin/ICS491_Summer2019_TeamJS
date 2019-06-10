from django.shortcuts import render, redirect
from yeelight import Bulb
from yeelight import *
from django.contrib.auth.decorators import login_required
from adddevice.models import AddDevice
from django.contrib.auth.models import User

@login_required(login_url="/accounts/login")
def light_on(request):
    userIP = AddDevice.objects.get(owner=request.user).ip
    bulb = Bulb(userIP)

    bulb.turn_on()

    return redirect('lightthemes:lighthome')

@login_required(login_url="/accounts/login")
def light_off(request):
    userIP = AddDevice.objects.get(owner=request.user).ip
    bulb = Bulb(userIP)

    bulb.turn_off()

    return redirect('lightthemes:lighthome')

# Create your views here.
@login_required(login_url="/accounts/login")
def lighttheme_list(request):
    return render(request, 'lightthemes/lighttheme_list.html')

@login_required(login_url="/accounts/login")
def fire_theme(request):
    return redirect('lightthemes:lighthome')

@login_required(login_url="/accounts/login")
def rain_theme(request):
    return redirect('lightthemes:lighthome')

@login_required(login_url="/accounts/login")
def sun_theme(request):

    userIP = AddDevice.objects.get(owner=request.user).ip
    bulb = Bulb(userIP)

    duration = 1000
    brightness = 100

    transitions = [
    RGBTransition(255, 193, 0, duration=duration, brightness=brightness),
    RGBTransition(255, 154, 0, duration=duration, brightness=brightness),
    RGBTransition(255, 116, 0, duration=duration, brightness=brightness),
    RGBTransition(255, 77, 0, duration=duration, brightness=brightness),
    RGBTransition(255, 0, 0, duration=duration, brightness=brightness),
    RGBTransition(255, 77, 0, duration=duration, brightness=brightness),
    RGBTransition(255, 116, 0, duration=duration, brightness=brightness),
    RGBTransition(255, 154, 0, duration=duration, brightness=brightness),
    ]

    flow = Flow(
    count=50,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')
