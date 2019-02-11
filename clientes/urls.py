from django.urls import path
from .views import client_list, client_new, client_update, client_delete

urlpatterns = [
    path('list/', client_list, name="client_list"),
    path('new/', client_new, name="client_new"),
    path('update/<int:id>/', client_update, name="client_update"),
    path('delete/<int:id>/', client_delete, name="client_delete"),
]
