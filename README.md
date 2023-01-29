# GPU-and-CPU-Monitroing-with-Ardunio

 Hello, in this project, I tried to make a project to monitor the parts of computer components with Arduino from with the help of ChatGPT, without any library knowledge.

 After trying many different methods and libraries throughout the project, I realized that the most suitable one for me was to transmit the data to Arduino with OpenHardwareMonitor and wmi. Because most functional libraries suitable for this project can only work with Linux or cause incompatibility problems for AMD systems.
 
# Circuit Diagram 

![Circuit Diagram](https://user-images.githubusercontent.com/123881168/215335623-b8bf33ea-6f1d-4de5-b2ce-5770052a1427.JPG)

I used LCD Keypad Shield but also some more efficient LCD Screen could be use for more data monitoring.


# How It Is Work?

I have explained the places in the code that you can edit according to your needs, but to repeat, you can view data such as clock mhz, not just temperatures actually you can monitoring whole datas which are containing on openhardwaremonitor. Since I am using a 16x2 LCD screen, I did not want to take too much data and tire the Arduino UNO.


# !!!KEEP IN YOUR MIND OPENHARDWAREMONITOR SHOULD BE WORKING ON THE BACKGROUND!!!

https://openhardwaremonitor.org/downloads/

# EXAMPLE 

![WhatsApp Image 2023-01-29 at 18 11 11](https://user-images.githubusercontent.com/123881168/215335796-aaa71dc0-7cbc-4c1d-bc2d-560af1c8653b.jpeg)

