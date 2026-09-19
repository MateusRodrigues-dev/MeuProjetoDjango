from django.urls import path
from . import views  # O '.' significa 'importe da pasta atual'

urlpatterns = [
    # Quando alguém visitar a URL raiz deste app (ex: /), 
    # chame a função 'app_view' que está em 'views.py'.
    # O 'name' é um apelido opcional que usaremos mais tarde.
    path('', views.home_view, name='app'),
    path('perfil/', views.perfil_view , name ='perfil'),
    path('status/', views.status_view , name= 'status'),
    # Se você tivesse outras páginas neste app, você as adicionaria aqui:
    # ex: path('sobre/', views.sobre_view, name='sobre'),
    # ex: path('contato/', views.contato_view, name='contato'),
]