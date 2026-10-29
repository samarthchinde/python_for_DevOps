import psutil

# write a scipt which will tell the system info or system util

print("satrt")

def system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    
    system_info = {
    "cpu" : cpu,
    "memory" : memory,
    "disk" : disk
    }
    
    print(system_info)




