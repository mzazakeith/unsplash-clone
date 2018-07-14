from django.shortcuts import render
from django.http import HttpResponse, Http404

from gallery.models import Image, Location


def index(request):
    images = Image.show_images()
    title = "Beautiful Free Images & Pictures | Unsplash"
    return render(request, 'index.html', {"images": images , "title":title})


