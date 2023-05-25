def collect_diagnostics(device):
    print("Connecting to diagnostics server.")
    device.status_update()
    print("Sending status update to server.")
