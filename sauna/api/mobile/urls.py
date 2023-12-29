from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"device", views.DeviceMobileAPI)
router.register(r"saunasession", views.SaunaSessionMobileAPI)
router.register(r"reading", views.ReadingMobileAPI)

urlpatterns = [
    path("dashboard/", views.MobileDashboardAPI.as_view(), )
]
urlpatterns += router.urls
