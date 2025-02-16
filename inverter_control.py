import logging
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType
from deye_controller import SellProgrammer

_LOGGER = logging.getLogger(__name__)

class InverterControl:
    def __init__(self, ip, serial, mock=False):
        if mock:
            print("[MOCK MODE] Inverter initialized without real connection.")
            self.mock = True
            return

        self.inverter = SellProgrammer(ip, serial)
        self.mock = False

    def set_battery_mode(self, mode):
        if mode not in ["charge", "discharge", "idle"]:
            raise ValueError("Invalid mode. Choose from 'charge', 'discharge', or 'idle'.")

        power = 0 if mode == "idle" else (2500 if mode == "charge" else -2500)

        if self.mock:
            print(f"[MOCK MODE] Pretending to set mode: {mode} with power {power}")
        else:
            self.inverter.update_program(0, start_t='00:00', power=power, soc=50, grid_ch=True)
            self.inverter.upload_settings()

        print(f"Inverter mode set to {mode}")

def setup(hass: HomeAssistant, config: ConfigType):
    inverter_ip = config.get("billbuster_hassio", {}).get("ip", "192.168.1.108")
    inverter_serial = config.get("billbuster_hassio", {}).get("serial", 2799999999)


    def set_battery_mode(call: ServiceCall):
        mode = call.data.get("mode")
        power = call.data.get("power", 2500)  

        if mode not in ["charge", "discharge", "idle"]:
            _LOGGER.error("Invalid mode: %s", mode)
            return

        if mode == "idle":
            power = 0
        elif mode == "discharge":
            power = -abs(power)

        try:
            _LOGGER.info("Setting inverter mode to %s with power %dW", mode, power)
            inverter.update_program(0, start_t='00:00', power=power, soc=50, grid_ch=True)
            inverter.upload_settings()
        except Exception as e:
            _LOGGER.error("Failed to set inverter mode: %s - Exception: %s", mode, str(e))


    hass.services.register("inverter_control", "set_battery_mode", set_battery_mode)
    return True
