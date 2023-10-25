from django.urls import path
from . import views
# from .api_views import AppInfoList,AppInfoDetail

urlpatterns = [
    path('',views.index, name='index'),
    path('create', views.create, name ='create'),
    path('add', views.add, name ='add'),
    path('update/<int:id>', views.update, name ='update'),
    path('delete/<int:id>', views.delete, name ='delete'),
    path('appinfo/', views.search, name='search'),
    path('appinfo/<int:pk>', views.AppInfoDetail.as_view(), name='appinfo-detail')
]