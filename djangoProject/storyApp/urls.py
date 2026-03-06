from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generate/", views.generate, name="generate"),
    path("play/", views.play, name="play"),
    path("record/", views.record, name="record"),
    path("blob/", views.blob, name="blob"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)