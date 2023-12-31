from django.shortcuts import render, redirect
from django.http import HttpResponse, request, Http404
from django.template import loader
from django.contrib.auth import login, authenticate, logout,get_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Vehicle
from .forms import NewUserForm, VehicleForm

from django.contrib.auth.decorators import login_required


def index(request):
    vehicle_ids = Vehicle.objects.all()
    context = {
        "vehicle_ids": vehicle_ids,
    }
    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render(context, request))


def detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    context = {
        "car": vehicle
    }
    template = loader.get_template("polls/detail.html")
    return HttpResponse(template.render(context, request))


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="polls/register.html", context={"register_form": form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="polls/login.html", context={"login_form": form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("index")

def vehicleForm(request):
	if request.method == 'POST' :
		form = VehicleForm(request.POST, request.FILES)
		logged_user = get_user(request)
		if form.is_valid():
			vehicle = form.save(commit=False)
			vehicle.user = logged_user
			vehicle.save()
			return redirect("index")
		else :
			messages.error(request, "Invalide informations.")
	else:
		form = VehicleForm()
	return render(request, 'polls/vehicle_form.html', {'form': form})