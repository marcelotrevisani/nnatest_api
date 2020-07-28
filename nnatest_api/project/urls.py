from django.urls import include, path
from rest_framework.routers import DefaultRouter

from project import views


app_name = "project"

router = DefaultRouter()
router.register("project", views.ProjectView)

urlpatterns = [
    path("", include(router.urls)),
]