from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name='index'),
    path("post/<str:pk>", views.post, name='post'),
    path("myposts/", views.myposts, name='myposts'),
    path('upload/', views.upload,name="upload"),
    path('addpost/', views.addpost, name='addpost'),
    path("deletepost/<str:pk>", views.deletePost, name='deletepost'),
    path("mobiles/", views.mobiles, name='mobiles'),
    path("games/", views.games, name='games'),
    # path("gadgets/", views.gadgets, name='gadgets'),
    path("search/", views.search, name='search')
    
]