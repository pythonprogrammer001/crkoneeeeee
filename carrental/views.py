from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from urllib.parse import quote

from service.models import *
from django.db.models import Q
from PIL import Image


def home_site(request):
    return render(request,"index.html")
