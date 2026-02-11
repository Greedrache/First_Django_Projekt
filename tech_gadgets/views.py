import json
from django.shortcuts import redirect #render
from django.http import  HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from json  import dumps
from django.utils.text import slugify
from django.urls import reverse

from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse("Hello World")

def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
      new_slug = slugify(gadgets[gadget_id]["name"])
      new_url = reverse("gadget_slug_url", args=[new_slug])
      return redirect(new_url) #slugs bindestrich statt leerzeichen
    return HttpResponseNotFound("Gadget not found")



def single_slug_view(request, gadget_slug=""):
   
   if request.method == "GET":
       gadget_match = None

       for gadget in gadgets:
           if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget
    
       if gadget_match:
        return JsonResponse(gadget_match) #slugs bindestrich statt leerzeichen
       raise Http404("Gadget not found")
   

   if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"Received data: {data}")
            return JsonResponse({"response": "Das Gadget wurde erfolgreich empfangen"})
        except:
            return JsonResponse({"response": "Fehler beim Verarbeiten der Daten"}, status=400 )


def single_post_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"Received data: {data}")
            return JsonResponse({"response": "Das Gadget wurde erfolgreich empfangen"})
        except:
            return JsonResponse({"response": "Fehler beim Verarbeiten der Daten"}, status=400)
    return JsonResponse({"response": "Nur POST-Anfragen erlaubt"}, status=405)

