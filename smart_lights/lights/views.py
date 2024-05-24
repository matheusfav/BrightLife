# lights/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Lamp

@login_required
def lamp_list(request):
    lamps = Lamp.objects.filter(user=request.user)
    return render(request, 'lamp_list.html', {'lamps': lamps})

@login_required
def lamp_detail(request, lamp_id):
    lamp = Lamp.objects.get(id=lamp_id, user=request.user)
    return render(request, 'lamp_detail.html', {'lamp': lamp})
