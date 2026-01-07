from settings import MIKROTIK_IP, MIKROTIK_USER
from settings import MIKROTIK_PASSWORD
from iotcore.mikrotik import router


mikrotik = router(
    ip=MIKROTIK_IP,
    user=MIKROTIK_USER,
    password=MIKROTIK_PASSWORD)

