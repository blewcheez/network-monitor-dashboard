import json
from ping3 import ping 
import speedtest
import psutil 
from datetime import datetime     

def collect_data():
  # Ping test 
  latency = ping("8.8.8.8") * 1000 #ms 
  
  # Speed test
  st = speedtest.Speedtest()
  download_speed = st.download() / 1_000_000 #Mbps 
  upload_speed = st.upload() / 1_000_000 
  
  # System Usage 
  cpu = psutil.cpu_percent()
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  
  # Save Data
  data = {
      "time": datetime.now().strftime("%Y-%m-%d %H: %M: %S"),
      "ping_ms": round(latency, 2),
      "download_mbps": round(download_speed, 2), 
      "upload_mbps":round(upload_speed, 2), 
      "cpu_percent": cpu, 
      "memory_percent": memory, 
      "disk_percent": disk, 
  }
  
  # Save file 
  with open("data.json", "a") as f: 
      f.write(json.dumps(data) + "\n")
    
if __name__== "__main__":
      collect_data()
      print("Data collected!")
    
    # end of code 