from django.urls import path
from apps.persona.views import index_persona

urlpatterns = [
    path('', index_persona),
]
