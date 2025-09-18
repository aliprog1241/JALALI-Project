from django.urls import path
from .views import BirthdayListView, BirthdayCreateView, BirthdayUpdateView, BirthdayDeleteView

urlpatterns = [
    path('', BirthdayListView.as_view(), name='home'),
    path('add/', BirthdayCreateView.as_view(), name='add_birthday'),
    path('edit/<int:pk>/', BirthdayUpdateView.as_view(), name='edit_birthday'),
    path('delete/<int:pk>/', BirthdayDeleteView.as_view(), name='delete_birthday'),
]
