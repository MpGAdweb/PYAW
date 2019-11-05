from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('Projects/<str:slug>/', views.detail),
    path('Sobre', views.about, name='about'),
    path('Criacao-de-sites', views.webdesign, name='webdesign'),
    path('Links-Patrocinados', views.paidads, name='paidads'),
    path('Email-Marketing', views.emkt, name='emkt'),
    path('Identidade-Visual', views.iviusal, name='ivisual'),
    path('Contato', views.contactPage, name='contact'),
    path('Otimização-SEO', views.seopage, name='seo'),
    path('robots.txt',TemplateView.as_view(template_name="site/robots.txt"),{'mimetype': 'text/plain'})
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
