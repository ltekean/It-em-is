from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import views

urlpatterns = [
    path('api/token/', views.CustomTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.Userview.as_view()),
    path('mock/', views.mockview.as_view()),
    path('follow/<int:user_id>/', views.followView.as_view(), name='follow_view'),
    # path('profilemodify/<int:user_id>/', views.profileModifyView.as_view(), name='profile_modify'),
]
