from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import to_do_data
# Create your views here.


def to_do_list(request):
    to_do_list = to_do_data.objects.all()
    return render(request, "test.html", {"to_do_list": to_do_list})
