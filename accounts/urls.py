from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("user-registation", UserRegistration, basename="User")

urlpatterns = router.urls 