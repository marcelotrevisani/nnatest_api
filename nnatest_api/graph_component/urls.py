from django.urls import include, path
from rest_framework.routers import DefaultRouter

from graph_component.views.builtin_view import BuiltinComponentView
from graph_component.views.edge_view import EdgeView
from graph_component.views.input_view import InputView
from graph_component.views.link_view import LinkView
from graph_component.views.node_view import NodeView
from graph_component.views.output_view import OutputView

app_name = "graph_component"

router = DefaultRouter()
router.register("node", NodeView)
router.register("edge", EdgeView)
router.register("link", LinkView)
router.register("input", InputView)
router.register("output", OutputView)
router.register(r"components", BuiltinComponentView, basename="components")

urlpatterns = [
    path("", include(router.urls)),
]

