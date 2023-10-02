from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from orders.views import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customer")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls))
]
