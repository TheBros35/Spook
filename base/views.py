from django.shortcuts import render
from .models import Computer


def index(request):
    computers = Computer.objects.all()
    context = {
        'computers': computers,
    }
    return render(request=request, template_name='index.html', context=context)
