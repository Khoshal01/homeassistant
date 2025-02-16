from inverter_control import InverterControl

# Example IP and Serial (not used in mock mode)
INVERTER_IP = "192.168.1.108"
INVERTER_SERIAL = 2799999999

# Initialize the controller in MOCK MODE
controller = InverterControl(INVERTER_IP, INVERTER_SERIAL, mock=True)

# Test different modes
controller.set_battery_mode("charge")
controller.set_battery_mode("discharge")  # Change to 'discharge' or 'idle' as needed
controller.set_battery_mode("idle")  # Change to 'discharge' or 'idle' as needed
# Change to 'discharge' or 'idle' as needed
