from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.first.views import CarAddPhoto, CarView, CarViewUpdateDelte, TestEmail

urlpatterns = [
    path('', CarView.as_view()),
    path('/<int:pk>', CarViewUpdateDelte.as_view()),
    path('/<int:pk>/photo', CarAddPhoto.as_view()),
    path('/test', TestEmail.as_view())
]
