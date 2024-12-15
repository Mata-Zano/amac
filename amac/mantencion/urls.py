from django.urls import path
from .views import *



urlpatterns = [
    path('mantencion/',mantencion, name="mantencion"),
    # path('addMantencion/',addMantencion, name="addMantencion"),
    # path('addProductMantencion/',addProductMantencion, name="addProductMantencion"),
    # path('AgregarCotizacion/',addTipo, name="addcotizacion"),

]