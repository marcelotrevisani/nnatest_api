from rest_framework import serializers

from graph_component.models.input import Input


class InputSerializers(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ("id", "name", "node", "arg_name", "py_type")
        read_only_fields = ("id",)
