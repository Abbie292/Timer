import time

seconds = int(input("Input Seconds: "))
mins = int(input("Input Minutes: "))
hours =int(input("Input Hours: "))

countdown = (mins*60)+(hours*60*60)+ seconds


for i in range(countdown):
    print(str(countdown - i) + " Seconds left")
    time.sleep(1)
print("Time is up!")