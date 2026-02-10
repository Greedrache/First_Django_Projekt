from django.shortcuts import redirect #render
from django.http import  HttpResponse, JsonResponse
from json  import dumps
from django.utils.text import slugify
from django.urls import reverse

from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse("Hello World")

def single_gadget_view(request, gadget_id):

    new_slug = slugify(gadgets[gadget_id]["name"])
    new_url = reverse("gadget_slug_url", args=[new_slug])
    return redirect(new_url) #slugs bindestrich statt leerzeichen

def single_slug_view(request, gadget_slug):
    gadget_match = {"result": "nothing found"}

    for gadget in gadgets:
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget
    return JsonResponse(gadget_match) #slugs bindestrich statt leerzeichen