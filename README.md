# Summary
This project takes advantage of the python libraries PySerial and Pyautogui to interface with arduino through serial communication and replace certain keyboard keys. With the use of an infrared receiver, I can now use a control remote to interact with the computer and select/open/close applications as well as access anything online.

For more information on PySerial check the documentation page: https://pythonhosted.org/pyserial/
For more information on Pyautogui cheak the following link: https://pyautogui.readthedocs.io/en/latest/

**Demo**

https://www.youtube.com/watch?v=THrF9m3o-4Q&feature=youtu.be

# Components

- UNO R3 Controller Board
- IR receiver
- remote control
- Breadboard
- Jumper wires
- USB Cable A-to-B

# Circuit Diagrams

**Schematic**
![](/media/fun_remote_schematic.PNG)

**Breadboard**
![](/media/fun_remote_breadboard.PNG)


**NOTE:** the HEX values are different from every remote control, if you are looking to use this project with your own remote open the serial monitor in the Arduino IDE and push the remote's buttons you are interested in programming. The button's HEX value will be displayed in the monitor. You can now replace the old HEX value in fun_remote_controller.py with the new ones so the program work with you own remote controller.
