import sounddevice as sd

def get_loopback_device():
    hostapis = sd.query_hostapis()
    for i, device in enumerate(sd.query_devices()):
        hostapi_name = hostapis[device['hostapi']]['name']
        if 'loopback' in device['name'].lower() and 'wasapi' in hostapi_name.lower():
            return i, device['name']
    raise RuntimeError("No WASAPI loopback device found.")

index, name = get_loopback_device()
print(f"Selected loopback device: {index} — {name}")
