import asyncio
from bleak import BleakScanner

async def scan_all_bluetooth_devices():
    print("Scanning for all BLE devices...")
    scanner = BleakScanner()
    devices = await scanner.discover()

    if devices:
        print(f"Found {len(devices)} devices:")
        for device in devices:
            print(f"  Name: {device.name or 'Unknown'}, Address: {device.address}")
    else:
        print("No devices found.")

if __name__ == "__main__":
    asyncio.run(scan_all_bluetooth_devices())
