import pywhatkit as kit

#pywhatkit is available in the python library. Before running the code it is necessary to 

#check whether you have downloaded the python3 module and pywhatkit library function onto the terminal.

print("Enter the number along with your country code:")
a=int(input())

print("Enter the text:")
b=str(input())

print("Enter the time in 24-hour format:(ex. 19:36)")
x,y=map(int,input().split(":"))

#In this specific code, I have imported pywhatkit as kit and used along one of its function "sendwhatmsg".

#Time should be mentioned in 24-hour format. Important note is that the mentioned time should be

#greater than one minute prior the mentioned time. 

kit.sendwhatmsg("+a","b",x,y)