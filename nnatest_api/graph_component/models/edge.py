from django.db import models

from graph_component.models.node import Node


class Edge(models.Model):
    parent = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name="edge_out"
    )
    child = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name="edge_in"
    )

    def __str__(self):
        return f"{self.parent} -> {self.child}"
