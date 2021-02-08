from django.urls import path
from person import views

urlpatterns = [
    path('post-person/', views.post_person),
    path('get-persons/', views.get_persons),
    path('get-put-delete/<int:pk>', views.get_put_delete_person),
    path('search-person', views.search_person)

]