# Django imports
from django.contrib import admin
from django.urls import path, include

# Projects imports
# from apps.erp.views import myFirstView

# Python imports

urlpatterns = [
    path('admin/', admin.site.urls),

    path('erp/', include('apps.erp.urls'))
]
