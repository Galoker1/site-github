from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main_page"),
    path('book/',book_list, name="book_list_url"),
    path('book/create/',BookCreate.as_view(),name='book_create_url'),
    path('book/<str:slug>/update/', BookUpdate.as_view(), name="book_update_url"),
    path('book/<str:slug>/delete/', BookDelete.as_view(), name="book_delete_url"),
    path('book/<str:slug>/', BookDetail.as_view(), name="book_detail_url"),

]
