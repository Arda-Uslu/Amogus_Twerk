import pyautogui as auto
import time as t
import keyboard as kyb

auto.FAILSAFE=False

scrsize=auto.size()
#auto.moveTo(0,0,5)
#auto.click(x=1,y=1,clicks=1,interval=15,button="right")
#auto.dragRel(-100,100,5)
#auto.scroll(-500)

mouselist=[0,0]

def mouse():
    while True:
        if kyb.is_pressed("s"):
                return
        x,y=auto.position()
        t.sleep(0.01)
        x1,y1=auto.position()
        while x==x1 and y==y1:
            if kyb.is_pressed("s"):
                return
            print(0)
            x2,y2=auto.position()
            if x2!=x1 and y2!=y1:
                break
        if kyb.is_pressed("s"):
                return
        print(1) 
        mouselist.append(x1)
        mouselist.append(y1)
        mouselist.append(x2)
        mouselist.append(y2)

mouse()
#print(mouselist[-1])
i =2
listlen=len(mouselist)
while i<listlen:
    print("X:",mouselist[i],"Y:",mouselist[i+1])
    #auto.click()
    i+=2
i=2
x=input()
if x=="s":
    while i <listlen:
        auto.moveTo(mouselist[i],mouselist[i+1],0.1)
