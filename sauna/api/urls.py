from django.urls import path, include

urlpatterns = [
    path('mobile/', include('sauna.api.mobile.urls')),
]
