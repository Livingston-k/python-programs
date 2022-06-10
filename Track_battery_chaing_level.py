import psutil #import psutil module by using this command pip install psutil run this command in terminal or cmd
import pyttsx3 #import pyttsx3 module by using this command pip install pyttsx3 run this command in terminal or cmd
import time

while True:
    Battery = psutil.sensors_battery()
    Percentage_of_battry = Battery.percent
    Pluged = Battery.power_plugged
    if Percentage_of_battry == 100 and Pluged is True:
        pyttsx3.speak("Your Battery is fully charged kindly unplug the charger")
    if Percentage_of_battry < 30 and Pluged is False:
        pyttsx3.speak("Your Battery is low please plug the charger")
    
    print(Percentage_of_battry)
    time.sleep(3)