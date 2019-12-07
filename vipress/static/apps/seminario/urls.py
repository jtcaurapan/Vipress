from django.urls import path
from apps.seminario.views import index_seminario, index, seminario_list, seminario_edit, seminario_delete, SeminarioList, SeminarioCreate, SeminarioUpdate, SeminarioDelete


urlpatterns = [
    path('nuevo/', SeminarioCreate.as_view()),
    path('index/', index, name='index'),
    path('listar/', SeminarioList.as_view(), name='seminario_listar'),
    path('editar/<pk>/', SeminarioUpdate.as_view(), name='seminario_editar'),
    path('eliminar/<pk>/', SeminarioDelete.as_view(), name='seminario_eliminar'),
]
