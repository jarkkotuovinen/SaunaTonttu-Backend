from django.db.models import Avg
from django_filters import rest_framework as dj_filter
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from ...models import Device, SaunaSession, Reading, FlutterSession, Progression, Badges


class DeviceMobileAPI(viewsets.ModelViewSet):
    serializer_class = serializers.DeviceSerializer
    queryset = Device.objects.filter(is_active=True)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        mac_address = serializer.validated_data['mac_address']
        try:
            device = Device.objects.get(mac_address=mac_address)
            device.mac_address = mac_address
            device.is_active = True
        except Device.DoesNotExist:
            device = Device.objects.create(user=self.request.user, **serializer.validated_data)
        device.save()
        return device

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class SaunaSessionMobileAPI(viewsets.ModelViewSet):
    serializer_class = serializers.SaunaSessionSerializer
    queryset = SaunaSession.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        sauna_session = serializer.save()
        avg_temp = Reading.objects.filter(session=sauna_session).aggregate(avg_temp=Avg('temp'))['avg_temp']
        avg_humid = Reading.objects.filter(session=sauna_session).aggregate(avg_humid=Avg('humidity'))['avg_humid']
        avg_pressure = Reading.objects.filter(session=sauna_session).aggregate(avg_pressure=Avg('pressure'))[
            'avg_pressure']
        sauna_session.duration = (sauna_session.end_time - sauna_session.start_time).total_seconds() / 60.0
        sauna_session.avg_temp = avg_temp
        sauna_session.avg_humid = avg_humid
        sauna_session.avg_pressure = avg_pressure
        sauna_session.save()

        # calories_burned = health_utils.calculate_calorie_burn(),
        # heartbit_increased = health_utils.calculate_heart_rate_increase(),
        # blood_flow_increased = health_utils.calculate_blood_flow_increase(),


class ReadingMobileAPI(viewsets.ModelViewSet):
    serializer_class = serializers.ReadingSerializer
    queryset = Reading.objects.all()
    filter_backends = (dj_filter.DjangoFilterBackend,)
    filterset_fields = ('session', 'device')

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class MobileDashboardAPI(APIView):

    def get(self, request):
        total_session = SaunaSession.objects.filter(user=self.request.user).count()
        longest_session = SaunaSession.objects.filter(user=self.request.user).order_by('-duration').first()
        highest_humidity = Reading.objects.filter(user=self.request.user).order_by('-humidity').first()
        highest_temp = Reading.objects.filter(user=self.request.user).order_by('-temp').first()
        highest_pressure = Reading.objects.filter(user=self.request.user).order_by('-pressure').first()
        highest_calorie_burn = SaunaSession.objects.filter(user=self.request.user).order_by('-calories_burned').first()

        return Response({
            "total_session": total_session,
            "longest_session": longest_session.duration if longest_session else "N/A",
            "highest_humidity": highest_humidity.humidity if highest_humidity else "N/A",
            "highest_temp": highest_temp.temp if highest_temp else "N/A",
            "highest_pressure": highest_pressure.pressure if highest_pressure else "N/A",
            "highest_calorie_burn": highest_calorie_burn.calories_burned if highest_calorie_burn else "N/A",
        }, status=status.HTTP_200_OK)

class FlutterSessionAPI(viewsets.ModelViewSet):
    serializer_class = serializers.FlutterSessionSerializer
    queryset = FlutterSession.objects.all()

    def get__queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class ProgressionAPI(APIView):
    #def post(self, request):
        
    def get(self, request):
        level = Progression.objects.filter(user=self.request.user)
        streak = Progression.objects.filter(user=self.request.user)
        badges = Badges.objects.filter(user=self.request.user)

        return Response({
            "level": level,
            "streak": streak,
            "badges": badges
        }, status=status.HTTP_200_OK)

class BadgesAPI(APIView):
    def get(self, request):
        badges = Badges.objects.filter(user=self.request.user)

        return Response({
            "badges": badges
        }, status=status.HTTP_200_OK)