##Deye Inverter Control - Home Assistant Integration

Overview
This project provides a Home Assistant integration for controlling a Deye inverter. It allows switching between charge, discharge, and idle states via Home Assistant automation.

Installation

1️⃣ Create a Virtual Environment & Install Dependencies
Ensure Python is installed, then run the following commands:
```sh
Create a virtual environment
python -m venv .venv

Activate the virtual environment
For Windows:
.venv\Scripts\activate
For macOS/Linux:
source .venv/bin/activate

Install all dependencies
pip install -r requirements.txt
```

2️⃣ Set Up Home Assistant Integration
1. Extract the `homeassistant.zip` file.
2. Copy the extracted `homeassistant` folder into your Home Assistant `config` directory.
3. Restart Home Assistant.
4. Navigate to **Settings > Devices & Services** and add the integration.

3️⃣ Switching from Mock Mode to Real Device
By default, the integration runs in **mock mode** (for testing without real hardware). To connect to a real inverter:
1. Open `inverter_control.py`.
2. Locate this line:
   ```python
   controller = InverterControl("192.168.1.108", 2799999999, mock=True)
   ```
3. Change `mock=True` to `mock=False`:
   ```python
   controller = InverterControl("192.168.1.108", 2799999999, mock=False)
   ```
4. Save the file and restart Home Assistant.

4️⃣ Testing the Integration
Run:
```sh
python test_inverter.py
```
Expected output in mock mode:
```
[MOCK MODE] Inverter initialized without real connection.
[MOCK MODE] Pretending to set mode: charge with power 2500
[MOCK MODE] Pretending to set mode: discharge with power -2500
[MOCK MODE] Pretending to set mode: idle with power 0
```

5️⃣ Using in Home Assistant Automations
Create an automation in Home Assistant that calls:
```yaml
alias: Set Inverter Mode
trigger:
  - platform: time_pattern
    minutes: "/10"
action:
  - service: inverter_control.set_battery_mode
    data:
      mode: "charge"
      power: 3000
```
Replace `charge` with `discharge` or `idle` as needed.

File Structure
```
/homeassistant/
 ├── inverter_control.py  # Main control script
 ├── test_inverter.py  # Testing script
 ├── pyproject.toml  # Project configuration
 ├── services.yaml  # Home Assistant service definitions
 ├── manifest.json  # Home Assistant integration manifest
 ├── utils.py  # Helper functions
 ├── enums.py  # Enum definitions
 ├── protocol.py  # Protocol handler
 ├── sell_programmer.py  # Communication handler
```

Support
For any issues, check Home Assistant logs or contact support.

---
🚀 Your Deye inverter control integration is now fully set up and ready to use!
