from django.urls import path

from modules.middleman import views

app_name = 'middleman'

urlpatterns = [
    path('google_food/', views.google_food.as_view(), name='google_food'),
]
