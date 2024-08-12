from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.pagination import PagePagination
from core.permissions.is_super_user_permission import IsSuperUserPermission
from core.services.email_service import EmailService

from apps.first.filter import CarFilter
from apps.first.models import CarModel
from apps.first.serializer import CarPhotoSerializer, CarSerializer


# Create your views here.
class CarView(ListAPIView):
    serializer_class = CarSerializer
    # queryset = CarModel.objects.less_than_price(30000).only_brand('Honda')
    queryset = CarModel.objects.all()
    pagination_class = PagePagination
    filterset_class = CarFilter
    permission_classes = [IsSuperUserPermission,]


    # def get(self, request ,*args, **kwargs):
    #     return super().list(request,*args, **kwargs)
    #
    # def post(self, request ,*args, **kwargs):
    #     return super().create(request,*args, **kwargs)
    #
    # def get_queryset(self):
    #     return car_filter(self.request.query_params)


class CarViewUpdateDelte(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

class CarAddPhoto(UpdateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)


class TestEmail(GenericAPIView):
    permission_classes = [AllowAny,]
    def get(self, *args, **kwargs):
        EmailService.send_test()
        return Response(status=status.HTTP_204_NO_CONTENT)