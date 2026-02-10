# Takes threshold values (CPU, disk, memory) from **user input**
# fetches system metrics using a Python library (example: `psutil`)
# Compares metrics against thresholds
# Prints the result to the **terminal**

import psutil

def cpu_usage():
    cpu_threshold = int(input("Enter the memory threshold"))
    current_cpu = psutil.cpu_percent(interval=1)
    print("current cpu percent is:",current_cpu)

    if current_cpu > cpu_threshold:
        print("CPU Usage Exceeded....")
    else:
        print("CPU usage is OK")

def disk_usage():
    disk_threshold = int(input("Enter the disk threshold"))
    current_disk = psutil.disk_usage('/').percent
    print("current Disk usage is:",current_disk)

    if current_disk > disk_threshold:
        print("Disk Usage Exceeded....")
    else:
        print("Disk usage is OK")

def memory_usage():
    memory_threshold = int(input("Enter the memory threshold"))
    current_memory = psutil.virtual_memory().percent
    print("current Memory usage is:",current_memory)

    if current_memory > memory_threshold:
        print("Memory Usage Exceeded....")
    else:
        print("Memory usage is OK")

cpu_usage()
disk_usage()
memory_usage()
