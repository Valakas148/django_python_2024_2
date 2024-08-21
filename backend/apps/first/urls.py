from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.first.views import CarView

urlpatterns = [
    path('', CarView.as_view(), name='car_list_create'),
    # path('/<int:pk>', CarViewUpdateDelte.as_view()),
    # # path('/<int:pk>/photo', CarAddPhoto.as_view()),
    # path('/test', TestEmail.as_view())
]
