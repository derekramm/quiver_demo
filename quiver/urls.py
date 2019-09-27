from django.urls import path

from quiver import views

app_name = 'quiver'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_detail/<uuid>', views.book_detail, name='book_detail'),
    path('note_detail/<uuid>', views.note_detail, name='note_detail'),
]
