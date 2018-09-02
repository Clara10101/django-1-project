import datetime
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from pracownicy import models
import json

def pokazEtaty(request):
    etaty=models.Etaty.objects.all()
    return render(request, 'etaty.html', locals())

def pokazZespoly(request):
    zespoly=models.Zespoly.objects.all()
    return render(request, 'zespoly.html', locals())

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pokazPracownikow(request):
    zespoly = models.Zespoly.objects.all()
    pracownicy_list = models.Pracownicy.objects.all()
    paginator = Paginator(pracownicy_list, 2) # Show 10 per page

    page = request.GET.get('page')
    try:
        pracownicy = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pracownicy = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pracownicy = paginator.page(paginator.num_pages)

    return render_to_response('pracownicy.html', {"pracownicy": pracownicy, "zespoly": zespoly})
    #return render(request, 'pracownicy.html', locals())

def pokazWszystko(request):
    pracownicy = models.Pracownicy.objects.all()
    etaty = models.Etaty.objects.all()
    zespoly = models.Zespoly.objects.all()
    return render(request, 'wszystko.html', locals())

def pokazPracownika(request, pk):
    pracownik=get_object_or_404(models.Pracownicy, pk=pk)
    szef_id = pracownik.ID_szefa
    return render(request, 'pracownik.html', locals())

def pokazZespol(request, pk):
    zespol=get_object_or_404(models.Zespoly, pk=pk)
    return render(request, 'zespol.html', locals())

def pokazEtat(request, pk):
    etat = get_object_or_404(models.Etaty, pk=pk)
    return render(request, 'etat.html', locals())

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

def ajaxZapiszPlaca(request):
    #zmiana pensji podstawowej, dodatkowej i zespolu dla pracownika
    if request.method == 'POST':
        pracownik=get_object_or_404(models.Pracownicy, pk=request.POST['pracownik'])
        zespoly = models.Zespoly.objects.all()
        new_zespol = int(request.POST['zespol'])
        pks = [int(z.pk) for z in zespoly]
        if new_zespol not in pks:
            return HttpResponse('2')
        zespol = get_object_or_404(models.Zespoly, pk=new_zespol)
        pracownik.placa_pod = int(request.POST['placa_pod'])
        pracownik.placa_dod = int(request.POST['placa_dod'])
        pracownik.ID_zespolu = zespol
        if (pracownik.placa_pod < 0 or pracownik.placa_dod < 0):
            return HttpResponse('2')
        else:
            pracownik.save()
            return HttpResponse('0')

