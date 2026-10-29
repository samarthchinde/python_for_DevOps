import psutil

# as a devops engineer ,check the cpu usage for sec and take the threshold form user and check that cpu is healthy or not
thereshold = float(input("enter the threshold value for cpu usage:"))
for i in range(5):
    if psutil.cpu_percent(interval=1) > thereshold:
        print("cpu is not healthy")
    else:
        print("cpu is healthy")
   
