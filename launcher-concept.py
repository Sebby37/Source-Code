from time import sleep
#setup stuff goes here | Concept File Designed By Seb C:
print("Politicizer | 2020 Politburo Inc")
print("Checking for updates...")
debugup = str(input("DEBUG ONLY | Is there an update avaliable (y/n): "))

if debugup == "y":
    upfound = True
else:
    upfound = False
#Here a server would be contacted and if there was an update it would be set to True
sleep(2.50)
if upfound == True:
    print("Update Found! Downloading update size: 52.38 megabytes")
    updat = 0
    appl = 0
    for i in range(100):
        print(updat,"% Done")
        updat += 1
        sleep(0.25)
    print("Update fully downloaded!")
    sleep(0.50)
    print("Applying Update")
    for j in range(100):
        print(appl,"% Applied")
        appl += 1
        sleep(0.1)
elif upfound == False:
    print("No updates found!")
    sleep(1.50)
print("Running politicizer...")
