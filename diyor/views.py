from django.shortcuts import render
from .models import Kitob
from django.http import HttpResponse


def kitob_list(request):
    kitoblar = Kitob.objects.all()
    output = ', '.join([kitob.nom for kitob in kitoblar])
    return HttpResponse(output)

def kitob_detail(request, pk):  
    try:
        kitob = Kitob.objects.get(pk=pk)
        output = f"Nom: {kitob.nom}, Muallif: {kitob.mu allif}, Nashr Yili: {kitob.nashr_yili}, Narx: {kitob.narx}"
        return HttpResponse(output) 
    except Kitob.DoesNotExist:
        return HttpResponse("Kitob topilmadi", status=404)
    
    