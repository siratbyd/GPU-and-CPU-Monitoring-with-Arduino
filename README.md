# GPU-and-CPU-Monitroing-with-Ardunio

 Hello, in this project, I tried to make a project to monitor the parts of computer components with Arduino from scratch with the help of ChatGPT, without any library knowledge.

 After trying many different methods and libraries throughout the project, I realized that the most suitable one for me was to transmit the data to Arduino with OpenHardwareMonitor and wmi. Because most functional libraries suitable for this project can only work with Linux or cause incompatibility problems for AMD systems.

# How It Is Work?

I have explained the places in the code that you can edit according to your needs, but to repeat, you can actually view data such as clock mHZ, not just temperatures. Since I am using a 16x2 LCD screen, I did not want to take too much data and tire the Arduino UNO.

#KEEP IN YOUR MIND OPENHARDWAREMONITOR SHOULD BE WORKING ON BACKGROUND.
