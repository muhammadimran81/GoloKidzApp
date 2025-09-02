from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world")


class HelloPak(View):
    def get(self, request):
        return HttpResponse("Hello Pak")

def home(request):
    form = ReservationForm()

    if request.method == 'Post':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    return render(request, 'index.html',{'form': form})
