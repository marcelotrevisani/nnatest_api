from django.urls import include, path
from rest_framework.routers import DefaultRouter

from runner.views.execution_steps_view import ExecutionStepsView
from runner.views.execution_view import ExecutionView
from runner.views.machine_view import MachineView
from runner.views.manager_view import ManagerView

app_name = "runner"

router = DefaultRouter()
router.register("manager", ManagerView)
router.register("machine", MachineView)
router.register("execution", ExecutionView)
router.register("execution-steps", ExecutionStepsView)

urlpatterns = [
    path("", include(router.urls)),
]