import re

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


def add(request):
    mac_address = request.GET['mac_address']
    name = request.GET['name']

    # Checks for valid mac address.
    is_valid_mac = re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower())
    is_valid_name = len(name) < 100
    if is_valid_mac and is_valid_name:
        computer = Computer(name=name, mac_address=mac_address)
        computer.save()
        return redirect('/')
    # else:
    # return render_template('error_format.jinja2', mac_address=mac_address)


def remove(request):
    mac_address = request.GET['mac_address']
    Computer.objects.filter(mac_address=mac_address).delete()
    return redirect('/')
