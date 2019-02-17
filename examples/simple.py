import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from decawave_1001_rjg import Decawave1001Driver, DwmLocationResponse


class Simple:
    def __init__(self):
        self.driver = Decawave1001Driver(22, 2)
        # self.driver.reset()

    def main(self):
        try:
            self.get_version()
            self.get_config()
            count = 0
            while count < 10:
                if self.driver.data_ready(50):
                    self.get_loc()
                    self.get_pos()
                    count = count + 1
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            self.driver.close()

    def get_status(self):
        status = self.driver.get_status()
        print('Network joined: {}. Location ready {}'.format(status.uwb_network_joined, status.location_ready))
        return status

    def get_config(self):
        config = self.driver.get_cfg()
        print('Tag: {}. Low Power {}. Loc Engine {}. LED {}. BLE {}. Firmware update {}'.format(
            config.tag, config.low_power_enabled, config.location_engine_enabled, config.led_enabled, config.ble_enabled, config.firmware_update_enabled))
        return config

    def get_version(self):
        version = self.driver.get_ver()
        print('Version: firmware {}, config {}, hardware {}'.format(version.get_firmware_version(), version.get_configuration_version(), version.get_hardware_version()))
        return version

    def get_distance(self) -> int:
        location_response = self.driver.get_loc()
        anchor = location_response.get_anchor_distances_and_positions()[0]
        print('{}, {}, {}'.format(anchor.distance(), anchor.quality_factor(), anchor.address()))
        return anchor.distance()

    def get_pos(self):
        response = self.driver.get_pos()
        position = response.get_position()
        co_ords = position.position()
        print('Position: {}, Quality {}'.format(co_ords, position.quality_factor()))

    def get_loc(self) -> DwmLocationResponse:
        location_response = self.driver.get_loc()
        position = location_response.get_tag_position()
        pos = position.position()
        distances = '{}, {}, {}, {}, '.format(position.quality_factor(), pos[0], pos[1], pos[2])
        for anchor in location_response.get_anchor_distances_and_positions():
            distances += '{:.0f}, '.format(anchor.distance())
        for anchor in location_response.get_anchor_distances_and_positions():
            distances += 'DW_{}, '.format(anchor.address())
        print(distances)
        return location_response


if __name__ == '__main__':
    Simple().main()
