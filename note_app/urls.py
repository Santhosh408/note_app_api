from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import UserProfileApiView,RegisterApiView,NotesApiView,SingleNoteApiView

urlpatterns = [
    path('tokens/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('register/',RegisterApiView.as_view()),
    path('user/',UserProfileApiView.as_view()),
    path('notes/',NotesApiView.as_view()),
    path('note/<int:pk>',SingleNoteApiView.as_view()),
]