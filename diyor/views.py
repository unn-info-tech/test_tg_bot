from django.shortcuts import render
from .models import Kitob
from django.http import HttpResponse


def kitob_list(request):
    kitoblar = Kitob.objects.all()
    output = ', '.join([kitob.nom for kitob in kitoblar])
    return HttpResponse(output)


    
