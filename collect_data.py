import json
from ping3 import ping
import speedtest
import psutil
from datetime import datetime
import os

def collect_data():
    latency = ping("8.8.8.8")
    latency_ms = round(latency * 1000, 2) if latency else None

    st = speedtest.Speedtest()
    download_speed = round(st.download() / 1_000_000, 2)
    upload_speed = round(st.upload() / 1_000_000, 2)

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ping_ms": latency_ms,
        "download_mbps": download_speed,
        "upload_mbps": upload_speed,
        "cpu_percent": cpu,
        "memory_percent": memory,
        "disk_percent": disk,
    }

    # Load existing data or start new list
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                all_data = json.load(f)
                if not isinstance(all_data, list):
                    all_data = [all_data]
            except json.JSONDecodeError:
                 all_data = []
    else:
        all_data = []

    all_data.append(data)

    with open("data.json", "w") as f:
        json.dump(all_data, f, indent=4) 

if __name__ == "__main__":
    collected_data = collect_data()  # now you have the data in a variable
    print("Data collected!")

