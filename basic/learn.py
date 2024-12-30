#Operating System Utilities
""""
import os

cwd = os.getcwd()  # get current working directory
print(cwd)

files = os.listdir(cwd)  # list all files in a directory
print(files)

absolute_path = os.path.abspath(cwd)
print(absolute_path)


#os.mkdir("Python Folder")  #create new folder

#os.rmdir("Python Folder")  #delete folder from dirctory


if os.path.exists("alice.txt"):
    print("File exists.")
else:
    print("File does not exist.")

path = os.path.join(cwd, "Python Folder", "alice.txt")

print("Full path: ",path)

"""

#system specific utilties
"""

import sys

print(sys.path)  #python search path

if len(sys.argv) <2:         #Exiting the program
    sys.exit("Error Not enough arguments!")

print(sys.argv[0])  # Command Line arguments
if len(sys.argv) >1:
    print("Arguments:", sys.argv[1:])
else:
    print("Nothing")

"""

#url library


import urllib.request

# Fetch content from a URL
url = "http://google.com"
response = urllib.request.urlopen(url)
content = response.read()  # Read the response content
print(content.decode('utf-8'))  # Decode bytes to string


#file download
#url = "https://www.google.lk/imgres?q=ajith&imgurl=https%3A%2F%2Fimg.mensxp.com%2Fmedia%2Fcontent%2F2021%2FAug%2FBest-Movies-Of-Thala-Ajith-6_610cf607c64a5.jpeg%3Fw%3D720%26h%3D1280%26cc%3D1&imgrefurl=https%3A%2F%2Fwww.mensxp.com%2Fampstories%2Fentertainment%2Fcelebrities%2F91626-ajith-kumar-highest-rated-best-movies.html&docid=5h9OnMdbVgQ43M&tbnid=PwatWKn-2Vrj-M&vet=12ahUKEwiy7KK7yM6KAxU5xjgGHdOsEtsQM3oECF4QAA..i&w=720&h=1280&hcb=2&ved=2ahUKEwiy7KK7yM6KAxU5xjgGHdOsEtsQM3oECF4QAA"
#urllib.request.urlretrieve(url)
#print("downloaded!")    

text = ufile.read(url)
print(text)
"""
#sub process Library

#import subprocess

# Run a shell command
#result = subprocess.run(["echo", "Hello, World!"],shell=True, capture_output=True, text =True)
#print("Output:", result.stdout)


"""




















