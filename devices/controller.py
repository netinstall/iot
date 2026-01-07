import settings
from yandex.devices import controller

controller = controller(settings.YANDEX_CONTROLLER_ID, settings.CONTROLLER_MAP)
