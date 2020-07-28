from django.contrib import admin

from graph_component.models.edge import Edge
from graph_component.models.input import Input
from graph_component.models.link import Link
from graph_component.models.node import Node
from graph_component.models.output import Output

admin.site.register(Node)
admin.site.register(Edge)
admin.site.register(Link)
admin.site.register(Input)
admin.site.register(Output)
