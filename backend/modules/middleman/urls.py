from django.urls import path

from modules.middleman.Domain import views

app_name = 'middleman'

urlpatterns = [
    path('google_food/', views.ExternalApiView.as_view(), name='google_food'),
]
