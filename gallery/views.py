from django.shortcuts import render
from django.http import HttpResponse, Http404

from gallery.models import Image, Location


def index(request):
    images = Image.show_images()
    title = "Beautiful Free Images & Pictures | Unsplash"
    return render(request, 'index.html', {"images": images , "title":title})


def image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'image.html', {"image": image})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get('image')
        searched_images = Image.search_image(category)
        message = f"{category}"
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})


