from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from core.pagination import PagePagination

from apps.first.filter import CarFilter
from apps.first.models import CarModel
from apps.first.serializer import CarSerializer


# Create your views here.
class CarView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    pagination_class = PagePagination
    filterset_class = CarFilter
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

    # def get(self, *args, **kwargs):
    #
    #     car = self.get_object()
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # def put(self, *args, **kwargs):
    #
    #     data = self.request.data
    #     car = self.get_object()
    #     serializer = CarSerializer(car, data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # def patch(self, *args, **kwargs):
    #     data = self.request.data
    #     car = self.get_object()
    #     serializer = CarSerializer(car, data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def delete(self, *args, **kwargs):
    #     self.get_object().delete()
    #     return Response('', status=status.HTTP_204_NO_CONTENT)