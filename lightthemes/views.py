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

@login_required(login_url="/accounts/login")
def lighttheme_list(request):
    return render(request, 'lightthemes/lighttheme_list.html')

@login_required(login_url="/accounts/login")
def fire_theme(request):

    userIP = AddDevice.objects.get(owner=request.user).ip
    bulb = Bulb(userIP)

    duration = 1000
    brightness = 100

    transitions = [
    RGBTransition(255,0,0, duration=duration, brightness=brightness),
    RGBTransition(255,90,0, duration=duration, brightness=brightness),
    RGBTransition(255,154,0, duration=duration, brightness=brightness),
    RGBTransition(255,206,0, duration=duration, brightness=brightness),
    RGBTransition(255,232,8, duration=duration, brightness=brightness),
    RGBTransition(255,206,0, duration=duration, brightness=brightness),
    RGBTransition(255,154,0, duration=duration, brightness=brightness),
    RGBTransition(255,90,0, duration=duration, brightness=brightness),
    RGBTransition(255,0,0, duration=duration, brightness=brightness),
    ]

    flow = Flow(
    count=50,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')

@login_required(login_url="/accounts/login")
def rain_theme(request):

    userIP = AddDevice.objects.get(owner=request.user).ip
    bulb = Bulb(userIP)

    duration = 1000
    brightness = 100

    transitions = [
    RGBTransition(23, 80, 91, duration=duration, brightness=brightness),
    RGBTransition(11, 64, 87, duration=duration, brightness=brightness),
    RGBTransition(5, 52, 85, duration=duration, brightness=brightness),
    RGBTransition(0, 38, 79, duration=duration, brightness=brightness),
    RGBTransition(0, 25, 78, duration=duration, brightness=brightness),
    RGBTransition(0, 38, 79, duration=duration, brightness=brightness),
    RGBTransition(5, 52, 85, duration=duration, brightness=brightness),
    RGBTransition(11, 64, 87, duration=duration, brightness=brightness),
    ]

    flow = Flow(
    count=50,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')

@login_required(login_url="/accounts/login")
def sun_theme(request):

    userIP = AddDevice.objects.get(owner=request.user).ip
    bulb = Bulb(userIP)

    duration = 1000
    brightness = 100

    transitions = [
    RGBTransition(100, 96, 48, duration=duration, brightness=brightness),
    RGBTransition(100, 89, 41, duration=duration, brightness=brightness),
    RGBTransition(100, 80, 32, duration=duration, brightness=brightness),
    RGBTransition(99, 69, 20, duration=duration, brightness=brightness),
    RGBTransition(98, 59, 11, duration=duration, brightness=brightness),
    RGBTransition(98, 53, 3, duration=duration, brightness=brightness),
    ]

    flow = Flow(
    count=50,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')
