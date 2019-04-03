import cv2,math
import matplotlib.pyplot as plt
import numpy as np
import pygame
import threading
import tkinter as tk


def scoreboard2(x,y,z):
    a=x
    b=y
    c=z

    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    l4 = tk.Label( frame, text="YOU ARE OUT" )
    l1 = tk.Label( frame, text="YOUR GESTURE" )
    l2 = tk.Label( frame, text="COMPUTER" )
    l3 = tk.Label( frame, text="FINAL SCORE" )
    text1=tk.Label(frame,text=a)
    text2=tk.Label(frame,text=b)
    text3=tk.Label(frame,text=c)
    l4.pack()
    l2.pack()
    text1.pack()
    l1.pack()
    text2.pack()
    l3.pack()
    text3.pack()




def scoreboard1(x,y,z):
    a=x
    b=y
    c=z

    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    l1 = tk.Label( frame, text="YOUR GESTURE" )
    l2 = tk.Label( frame, text="COMPUTER" )
    l3 = tk.Label( frame, text="YOUR TOTAL SCORE" )
    text1=tk.Label(frame,text=a)
    text2=tk.Label(frame,text=b)
    text3=tk.Label(frame,text=c)
    l2.pack()
    text1.pack()
    l1.pack()
    text2.pack()
    l3.pack()
    text3.pack()



def scoreboard3(x,y,z):
    a=x
    b=y
    c=z

    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    l1 = tk.Label( frame, text="OPPS COMPUTER WON THE GAME" )
    l2 = tk.Label( frame, text="YOUR GESTURE" )
    l3 = tk.Label( frame, text="COMPUTER" )
    l4 = tk.Label( frame, text="COMPUTER FINAL SCORE" )
    text1=tk.Label(frame,text=a)
    text2=tk.Label(frame,text=b)
    text3=tk.Label(frame,text=c)
    l1.pack()
    l2.pack()
    text2.pack()
    l3.pack()
    text1.pack()
    l4.pack()
    text3.pack()

def scoreboard4(x,y,z):
    a=x
    b=y
    c=z
    global Final_Score
    global Score
    ss=Score
    m=Final_Score-Score
    mm=m+1
    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    l4 = tk.Label( frame, text="RUNS NEEDED TO WIN" )
    l1 = tk.Label( frame, text="YOUR GESTURE" )
    l2 = tk.Label( frame, text="COMPUTER" )
    l3 = tk.Label( frame, text="COMPUTER TOTAL SCORE" )
    text1=tk.Label(frame,text=a)
    text2=tk.Label(frame,text=b)
    text3=tk.Label(frame,text=c)
    text4=tk.Label(frame,text=mm)

    l2.pack()
    text1.pack()
    l1.pack()
    text2.pack()
    l3.pack()
    text3.pack()
    l4.pack()
    text4.pack()



blurValue = 35
bow = 0
Score = 0
Fianl_Score = 0
Comp_Score=0

print('Press Esc to quit.')

cap = cv2.VideoCapture(0)
while True:

    ret, img = cap.read()
    cv2.rectangle(img,(400,400),(100,100),(0,255,0),0)
    crop = img[100:400, 100:400]
    grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grey, (blurValue, blurValue), 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    max_area = -1
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    cnt=contours[ci]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(crop,(x,y),(x+w,y+h),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(255,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,255,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        # cv2.line(drawing,start,end,[0,255,0],2)
        # cv2.circle(drawing,far,5,[0,0,255],-1)
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop,far,1,[255,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop,start,end,[255,255,0],2)
        #cv2.circle(crop,far,5,[0,0,255],-1)
    if count_defects == 1:
        cv2.putText(img,"One", (75,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
    elif count_defects == 2:
        cv2.putText(img,"Two", (75,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
    elif count_defects == 3:
        cv2.putText(img,"Three", (75,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(img,"Four", (75,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
    elif count_defects == 5:
        cv2.putText(img,"Five", (75,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
    else:
        cv2.putText(img,"Zero", (75,50),cv2.FONT_HERSHEY_DUPLEX, 2, 2)

    cv2.imshow('Gesture', img)

    # all_img = np.hstack((drawing, crop))
    # cv2.imshow('Contours', all_img)
    k = cv2.waitKey(10)
    if k == 27:
        break

    elif k == ord('b'):
        print(bow)
        if bow == 1:
                x = np.random.randint(5)+1
                guess = cv2.imread('%d.jpg' % x)
                cv2.imshow('Desktop',guess)
                print('Outcomes:',x,count_defects+1)


                if x != count_defects+1:
                    print( 'comp_Run',count_defects+1)
                    Score = Score+x
                    print( 'Computers_New_Score:',Score)
                    if Score > Final_Score:
                        print('Computer Wins.')
                        root=tk.Tk()
                        scoreboard3(x,count_defects+1,Score)
                        root.mainloop()

                    else:
                        root=tk.Tk()
                        scoreboard4(x,count_defects+1,Score)
                        root.mainloop()

                else:
                    print('Out!')
                    Comp_Score = Score
                    print('Final_Computer_Score',Comp_Score)
                    print('Your_Final_Score_was',Final_Score)
                    if Final_Score>Comp_Score:
                        print('you win by ',Final_Score-Comp_Score,' Runs.')
                        break
                    else:
                        print('This is a Draw.')
                        break
        if bow == 0:

            x = np.random.randint(5)+1
            guess = cv2.imread('%d.jpg' % x)
            cv2.imshow('Desktop',guess)
            print('Outcomes:',x,count_defects+1)

            if x != count_defects+1 :
                print( 'Run:',count_defects+1)
                Score = Score+count_defects+1
                print( 'New_Score:',Score)
                root=tk.Tk()
                scoreboard1(x,count_defects+1,Score)
                root.mainloop()

            else:
                print('Out!')
                Final_Score = Score
                Score = 0
                print( 'Final Score',Final_Score)
                print('Now your bowling turn')
                bow = 1
                root=tk.Tk()
                scoreboard2(x,count_defects+1,Final_Score)
                root.mainloop()


cap.release()
cv2.destroyAllWindows()
