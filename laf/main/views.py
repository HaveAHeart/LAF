from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Ad


# Create your views here.


def index(request):
    latest_ads = Ad.objects.order_by('-time')[:20]
    context = {'latest_ads': latest_ads}
    return render(request, 'main/index.html', context)


def search(request):
    inName = request.POST['searchText']
    if inName is '':
        latest_ads = Ad.objects.order_by('-time')[:20]
    elif inName is not '':
        inName = str(inName)
        latest_ads = Ad.objects.filter(type=inType).filter(name=inName).order_by('-time')[:20]
    else:
        latest_ads = Ad.objects.filter(type=inType).order_by('-time')[:20]
    context = {'latest_ads': latest_ads}
    return render(request, 'main/index.html', context)


def newItemPage(request):
    context = {}
    return render(request, 'newItem/newItem.html', context)


def generate(request):
    ad = Ad()
    ad.name = str(request.POST['inName'])
    ad.location = str(request.POST['inLocation'])
    ad.type = str(request.POST['inType'])
    ad.email = str(request.POST['inEmail'])
    ad.phone = str(request.POST['inPhone'])
    ad.vkID = str(request.POST['inVKID'])
    ad.description = str(request.POST['inDescription'])
    ad.time = timezone.now()
    ad.generateID()
    ad.save()
    return index(request)


def details(request):
    return render(request, 'main/index.html', context={})
