from django.urls import path
from apps.seminario.views import index_seminario, index, seminario_list, seminario_edit, seminario_delete


urlpatterns = [
    path('', index_seminario),
    path('index/', index, name='index'),
    path('listar/', seminario_list, name='seminario_listar'),
    path('editar/<int:id_seminario>/', seminario_edit, name='seminario_editar'),
    path('eliminar/<int:id_seminario>/', seminario_delete, name='seminario_eliminar'),
]
