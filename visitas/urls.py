from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', RedirectView.as_view(url='cadastro/', permanent=False), name='index'),
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
]