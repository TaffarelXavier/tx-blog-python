"""hospitais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from hospitalapp.views import index, criar_post, editar_post, deletar_post
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='hospitais/index.html')),
    path('blog/', index, name="blog"),
    path('criar_post/', criar_post, name="criar_post"),
    path('editar/<int:id>', editar_post, name="editar"),
    path('deletar/<int:id>', deletar_post, name="deletar"),
    path('', include('usuarios.urls')),
    url(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
