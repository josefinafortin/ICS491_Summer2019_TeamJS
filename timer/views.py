from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def timer_view(request):
    return render(request, 'timer/timer.html')
