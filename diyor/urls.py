from django.urls import path
from .views import kitob_list

urlpatterns = [
    path('kitoblarim/', kitob_list),
]