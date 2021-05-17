
from django.urls import path
from . import views

# for importing jwt views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # for creating jwt access and refresh token
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), # for creating jwt access token again from refresh token
    path('api/notes/', views.Note.as_view(), name='note'),
    path('api/details/<int:id>/', views.DetailNote.as_view(), name='note_details'),
]