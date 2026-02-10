from django.urls import path
from .views import single_slug_view, start_page_view, single_gadget_view

urlpatterns = [
    path('', start_page_view),
    path('gadget/<int:gadget_id>', single_gadget_view),
    path('gadget/<slug:gadget_slug>', single_slug_view, name="gadget_slug_url")
      #integer wichtig damit Programm weiß, dass es sich um eine Zahl handelt
      #string wandelt Buchstaben in string um, aber auch Zahlen in string, deswegen int
]