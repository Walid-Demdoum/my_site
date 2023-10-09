from django.shortcuts import render
from django.http import HttpResponse,request,Http404
from django.template import loader
from .models import Vehicle


def index(request):
    vehicle_ids = Vehicle.objects.all()
    context = {
        "vehicle_ids":vehicle_ids,
    }
    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render(context,request))

def detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    context = {
        "car":vehicle
    }
    template = loader.get_template("polls/detail.html")
    return HttpResponse(template.render(context,request))