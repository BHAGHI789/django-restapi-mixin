from django.urls import path
from app import views
urlpatterns=[
    path('',views.Data_List.as_view()),
    path('add',views.Data_create.as_view()),
    path('re/<int:pk>/',views.Data_Retrive.as_view()),
    path('up/<int:pk>/',views.Data_update.as_view()),
    path('de/<int:pk>/',views.Data_delete.as_view())
]