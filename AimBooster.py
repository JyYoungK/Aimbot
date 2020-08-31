import pyautogui as pag
from PIL import ImageGrab
import keyboard
from time import sleep

SB = 1 
shot = 0 # Value that determines if the target has found
start = (670, 446) # Left/Top grid value
end = (1248, 847) # Right/Bottom grid value
rgb_value = (255, 219, 195) #rgb value of target

x,y = pag.position()
print((x,y))

sleep(2)

##while SB == 1:
##    screen = ImageGrab.grab() # Screen capture
##    for i in range (start[0],end[0],10):
##        for j in range (start[1],end[1], 10):
##            rgb = screen.getpixel((i,j)) # Gathering rgb value from the grid
##            if abs(rgb[0] - rgb_value[0])+abs(rgb[1]-rgb_value[1])+abs(rgb[2]-rgb_value[2])<80:
##                rgb = screen.getpixel((i+3,j))
##                if abs(rgb[0]-rgb_value[0])+abs(rgb[1]-rgb_value[1])+abs(rgb[2]-rgb_value[2])<80:
##                    pag.click((i+3,j)) # i+3 because the size of the ball is changing
##                    shot = 1
##                    break
##            if shot == 1:# Found target, reset
##                shot = 0
##                break
##        if keyboard.is_pressed('F3'): #terminate
##            SB = 0
##            break
