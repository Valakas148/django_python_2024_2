from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import ActivateUserView, RecoverPasswordRequestView, RecoverPasswordView, SocketView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recovery', RecoverPasswordRequestView.as_view()),
    path('/recovery/<str:token>', RecoverPasswordView.as_view()),
    path('/token', SocketView.as_view())
]

