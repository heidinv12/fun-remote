import serial
import pyautogui
import time

conn = serial.Serial('com3', 9600)
time.sleep(2)

num = {
			'E318261B': '1',
			'FFA25D': '1',
			'511DBB': '2',
			'FF629D': '2',
			'EE886D7F': '3',
			'FFE21D': '3',
			'52A3D41F': '4',
			'FF22DD': '4',
			'D7E84B1B': '5',
			'D78FE1FE': '5',
			'20FE4DBB': '6',
			'49DA4': '6',
			'F076C13B': '7',
			'FFE01F': '7',
			'A3C8EDDB': '8',
			'E5CFBD7F': '9',
			'97483BFB': '0',
			}

# gets the signal and removes spaces
def getInput():
	input = str(conn.readline())
	clean_input = input.strip() 
	print clean_input
	
	return clean_input

# select an action depending on the signal input	
def runProcess():
	while True:
		clean_input = getInput()
		try:
			# * button = WinKey, accesses task-bar apps
			if 'C101E57B' in clean_input:
				flag = True
				while flag:
					print "Input app position in taskbar"
					taskvar = getInput()
					try:
						if taskvar: 
							pyautogui.hotkey('win', num[taskvar])
							flag = False
						else:
							continue
					except KeyError:
						print "KeyError " + taskvar
						continue
			# 0 button = esc
			if '97483BFB' in clean_input:
				pyautogui.press('esc') 
			# 1 button = close app
			if 'E318261B' in clean_input:
				pyautogui.hotkey('alt', 'f4')
			#go to home of browser if button 2 is pressed
			if '511DBB' in clean_input:
				pyautogui.press('browserhome')
			# 5 button = space bar
			if 'D7E84B1B' in clean_input:
				pyautogui.press('space')
			# # button = tab
			if 'F0C41643' in clean_input:
				pyautogui.press('tab') 
			# OK button = enter
			if '488F3CBB' in clean_input:
				pyautogui.press('enter') 
			# up arrow button
			if '3D9AE3F7' in clean_input:
				pyautogui.press('up') 
			# down arrow button
			if '1BC0157B' in clean_input:
				pyautogui.press('down') 
			# left arrow button
			if '8C22657B' in clean_input:
				pyautogui.press('left') 
			# right arrow button
			if '449E79F' in clean_input:
				pyautogui.press('right') 		
		
		except Exception:
			print clean_input
			continue
		input = ''
	
	
if __name__ == "__main__":
	runProcess()
