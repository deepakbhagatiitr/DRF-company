# api/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CompanyViewSet, EmployeeViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)  # Register the viewset with a URL endpoint
router.register(r'employees', EmployeeViewSet)
# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
