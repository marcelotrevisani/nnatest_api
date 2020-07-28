from rest_framework import serializers

from graph_component.models.node import Node
from project.serializers import ProjectPKField


class NodeSerializers(serializers.ModelSerializer):
    edge_out = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        allow_empty=True,
    )
    edge_in = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )
    project = ProjectPKField()
    inputs = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )
    outputs = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )

    class Meta:
        model = Node
        fields = (
            "id",
            "name",
            "name_component_builtin",
            "project",
            "x_position",
            "y_position",
            "height",
            "width",
            "edge_out",
            "edge_in",
            "inputs",
            "outputs",
        )
        read_only_fields = (
            "id",
            "edge_out",
            "edge_in",
            "inputs",
            "outputs"
        )
