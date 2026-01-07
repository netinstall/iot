import re
import routeros_api


class router():

    def __init__(self, ip=None, user=None, password=None):
        self.ip = ip
        self.user = user
        self.password = password
        connection = routeros_api.RouterOsApiPool(ip, username=user, password=password, plaintext_login=True)
        self.api = connection.get_api()

    def command(self, command):
        command = re.sub(" ", "/", command)
        return self.api.get_resource(command).get()


    def get_lease_macs(self):
        MIKROTIK_LEASE_CMD = "/ip dhcp-server lease"
        return [lease.get("active-mac-address") for lease in self.command(MIKROTIK_LEASE_CMD)]


    def get_wifi_registration_macs(self):
        mac_address_list = []
        MIKROTIK_LEASE_CMD = "/interface wireless registration-table print; /quit"
        for item in str(self.ssh_command(MIKROTIK_LEASE_CMD)).split():
            if re.search(":.*:", item):
                mac_address_list.append(item)
        return mac_address_list

