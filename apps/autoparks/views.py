from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from core.permissions.is_admin_or_wr_only import IsAdminOrWrOnly

from apps.autoparks.models import AutoPark
from apps.autoparks.serializer import AutoParkSerializer
from apps.first.serializer import CarSerializer

# Create your views here.


class AutoParksView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoPark.objects.all()
    permission_classes = [IsAdminOrWrOnly,]


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoPark.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        seralizer = CarSerializer(data=data)
        seralizer.is_valid(raise_exception=True)
        seralizer.save(auto_park=auto_park)
        ap_serializer = AutoParkSerializer(auto_park)
        return Response(ap_serializer, status=status.HTTP_201_CREATED)