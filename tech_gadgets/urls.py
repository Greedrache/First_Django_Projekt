from django.urls import path
from .views import start_page_view, single_gadget_int_view, single_post_view, GadgetView, RedirectToGagdetView

urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGagdetView.as_view()),
    path('gadget/<int:gadget_id>', RedirectToGagdetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url")
      #integer wichtig damit Programm weiß, dass es sich um eine Zahl handelt
      #string wandelt Buchstaben in string um, aber auch Zahlen in string, deswegen int
]