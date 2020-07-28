import arca
from rest_framework.authentication import SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class BuiltinComponentView(ViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request, format=None):
        func_name = request.GET.get("name")
        components = serialize_component(arca.all_components)
        if func_name:
            return Response(components.get(func_name, {}))
        return Response(components)


def serialize_component(components):
    serialized_component = {}
    for k, v in components.items():
        m = v.metadata
        if isinstance(m.output, list):
            all_output = [{k: str(v) for k, v in t._asdict().items()} for t in m.output if t]
        else:
            all_output = [tuple(map(str, m.output))] if m.output else []
        serialized_component[k] = {
            "description": m.description if m.description else "",
            "function_name": m.func_name,
            "inputs": [{k: str(v) for k, v in t._asdict().items()} for t in m.input_list if t]  if m.input_list else [],
            "name": m.name,
            "outputs": all_output,
        }
    return serialized_component