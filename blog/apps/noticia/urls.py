
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('noticias/<int:id>/', views.noticiasdetalle, name='noticiasdetalle'),
    path("noticias/new", views.CrearNoticiaView.as_view(), name='CrearNoticiaView'),
    path('comentario/<int:id>/approve', views.comment_approve, name='comment_approve'),
    path('comentario/<int:id>/remove', views.comment_remove, name='comment_remove'),
    path('evento/', views.evento, name='evento'),
    path('contacto/', views.contacto, name='contacto'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)
