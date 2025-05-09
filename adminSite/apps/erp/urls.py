# Django imports
from django.urls import path

# Projects imports
from apps.erp.views import myFirstView

# Python imports

# -------------------------------------------------
urlpatterns = [
    path('prueba/', myFirstView)
]