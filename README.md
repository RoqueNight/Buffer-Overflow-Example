# Buffer-Overflow-Example
Simple BoF program written in C that demonstrates the difference between secure and unsecure code that makes a buffer overflow possible with a simple netcat reverse shell

# Unsecure.c
The code itself uses a function called "gets". It is used to scan or read a line of text from a standard input device and store it in the string variable. The problem is that it does not verify the amount of data it reads which enables data to overflow and cause a BoF. The buffer is set to 10 characters. If the user enters more than 10 characters , code will slip on and will execute the system() function which runs a netcat command to establish a reverse shell

# Secure.c
The "gets" function was replaced with fgets and was limited to only read the amount of data that was specificed inside the buffer (10). Any data that is longer than the buffer (10) , the program won't jump to the sustem() function and it will return the proper output

# The Attack (Unsecure.c)

- git clone https://github.com/RoqueNight/Buffer-Overflow-Example/
- cd Buffer-Overflow-Example
- gcc Unsecure.c -o unsecure
- ./unsecure

![alt text](tmp/unsecure.gif)

# Secure.c
./secure

![alt text](tmp/secure.gif)
