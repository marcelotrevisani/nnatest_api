from rest_framework import serializers

from graph_component.models.edge import Edge
from graph_component.models.node import Node


class EdgeSerializers(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )

    def validate(self, attrs):
        if not attrs.get("parent") or not attrs.get("child"):
            raise serializers.ValidationError("Parent of child should not be empty.")
        if attrs["parent"] == attrs["child"]:
            raise serializers.ValidationError("Parent and child cannot be the same.")
        parent_node = Node.objects.filter(id=attrs["parent"].id).values()[0]
        child_node = Node.objects.filter(id=attrs["child"].id).values()[0]
        if parent_node["project_id"] != child_node["project_id"]:
            raise serializers.ValidationError("Nodes should be in the same project.")
        return attrs

    class Meta:
        model = Edge
        fields = ("id", "parent", "child", "links")
        read_only_fields = ("id", "links")
        validators = []
