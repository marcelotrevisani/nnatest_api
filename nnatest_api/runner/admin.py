from django.contrib import admin

from runner.models.execution import Execution
from runner.models.machine import Machine
from runner.models.manager import Manager

admin.site.register(Manager)
admin.site.register(Machine)
admin.site.register(Execution)
