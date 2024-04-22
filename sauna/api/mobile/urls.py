from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"device", views.DeviceMobileAPI)
router.register(r"saunasession", views.SaunaSessionMobileAPI)
router.register(r"reading", views.ReadingMobileAPI)

#New views:
router.register(r"fluttersession", views.FlutterSessionAPI)


urlpatterns = [
    path("dashboard/", views.MobileDashboardAPI.as_view(), ),
    
    #New views:
    path("progression/", views.ProgressionAPI.as_view(), name='progression'),
    path("progression/badges", views.BadgesAPI.as_view(), name='badges')
]
urlpatterns += router.urls
