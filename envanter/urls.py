from django.urls import path
from . import views

urlpatterns = [
    path('', views.parca_listesi, name='parca_listesi'),
    path('ekle/', views.parca_ekle, name='parca_ekle'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('duzenle/<int:pk>/', views.parca_duzenle, name='parca_duzenle'),
    path('sil/<int:pk>/', views.parca_sil, name='parca_sil'),
    path('fotograf_sil/<int:pk>/', views.fotograf_sil, name='fotograf_sil'),
]
