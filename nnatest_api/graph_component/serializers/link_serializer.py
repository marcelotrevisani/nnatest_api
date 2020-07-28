from rest_framework import serializers

from graph_component.models.link import Link


class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ("id", "edge", "output", "input")
        read_only_fields = ("id",)
