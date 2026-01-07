from miio import DreameVacuum
import settings, secrets

marvin = DreameVacuum(settings.MARVIN_IP, secrets.MARVIN_TOKEN)
