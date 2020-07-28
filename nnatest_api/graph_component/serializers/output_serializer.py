from rest_framework import serializers

from graph_component.models.output import Output


class OutputSerializers(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = ("id", "name", "node", "arg_name", "py_type")
        read_only_fields = ("id",)
