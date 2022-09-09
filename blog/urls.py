from django.urls import path

from . import views
urlpatterns = [
    path('', views.ListView.as_view(), name='list_view'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail_view'),
    path('create/', views.CreatePost.as_view(), name='post_create'),
    path('<int:pk>/delete', views.PostDelete.as_view(), name='delete'),
    path('<int:pk>/update', views.PostUpdate.as_view(), name='update'),
]
