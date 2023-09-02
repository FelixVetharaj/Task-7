# Task-7- Function to create text file with current timestamp and read the text file and print in console

from datetime import datetime

#function to open a text file and write timestamp and close
def currentTimeStamp(timeStamp):
    f = open("felix.txt", "w+")
    f.write(str(timeStamp))
    f.close()

#function to read the content of textfile and print in console
def readTimeStamp(timeStamp):
    f = open("felix.txt", "r+")
    f1 = f.read()
    print(f1)

timeStamp = datetime.now()
#print(type(timeStamp))
currentTimeStamp(timeStamp)
readTimeStamp(timeStamp)