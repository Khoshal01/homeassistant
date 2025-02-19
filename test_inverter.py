import json
import os

# Define the shared folder path
SHARED_FOLDER = "/share/inverter_control"
STATE_FILE = os.path.join(SHARED_FOLDER, "state.json")

# Ensure the shared folder exists
os.makedirs(SHARED_FOLDER, exist_ok=True)

def save_state(mode, power):
    """Save inverter mode to state.json inside the shared folder."""
    state = {
        "mode": mode,
        "power": power
    }
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)
    print(f"State saved: {state}")

# Simulate inverter behavior
modes = [("charge", 2500), ("discharge", -2500), ("idle", 0)]
for mode, power in modes:
    print(f"[MOCK MODE] Pretending to set mode: {mode} with power {power}")
    save_state(mode, power)
