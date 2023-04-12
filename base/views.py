from django.shortcuts import render, redirect
from wakeonlan import send_magic_packet

from .models import Computer


def index(request):
    computers = Computer.objects.all()
    context = {
        'computers': computers,
    }
    return render(request=request, template_name='index.html', context=context)


def send(request):
    mac_address = request.GET['mac_address']
    send_magic_packet(mac_address)
    return redirect('/')