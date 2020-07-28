from django.db import models

from graph_component.models.output import Output
from graph_component.models.edge import Edge
from graph_component.models.input import Input


class Link(models.Model):
    edge = models.ForeignKey(Edge, on_delete=models.CASCADE, related_name="links")
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    output = models.ForeignKey(Output, on_delete=models.CASCADE)

    def __str__(self):
        return f"Link to edge {self.edge}"
