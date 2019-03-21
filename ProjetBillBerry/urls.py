"""ProjetBillBerry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from BillBerryImages.views import index, image_list_view, image_uploader_view, image_viewer_view, image_update_view
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index),
                  path('bilberryIndex', index, name='Home'),
                  path('imageListed', image_list_view, name='ImageList'),
                  path('imageViewer', image_viewer_view, name='ImageViewer'),
                  path('imageUploader', image_uploader_view, name='ImageUploader'),
                  path('imageUpdater', image_update_view, name='ImageUpdater')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
