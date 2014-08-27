# -*- coding: cp936 -*-
##creat by ljh in 2014-8-7
import math
import random
def changedegree(angle):
    if angle >180:
        return 0.0+angle -360.0
    else :     
        if angle <-180:
            return 0.0+angle +360.0
        else:
            return angle

def func(bullet_x,bullet_y,bullet_angle,bullet_speed,aim_x,aim_y,aim_angle,aim_spped,t):
    x = aim_x - bullet_x
    y = aim_y - bullet_y
    sita = math.degrees(math.atan(y/x))
    if x <0:
        if sita<0:
            sita = 180+sita
        else:
            sita = -180+sita
    minangle = 5
    
    angle1 = bullet_angle + minangle
    angle2 = bullet_angle - minangle   
    angle1 = changedegree(angle1)
    angle2 = changedegree(angle2)    
    j1 = changedegree(sita - angle1)
    j2 = changedegree(sita - angle2)
    
    if abs(j1) <abs(j2) :
        if abs(j1)<2*minangle:
            angle = sita
        else:
            angle_temp=bullet_angle
            x_temp=bullet_x
            y_temp=bullet_y
            for i in range(0,360/minangle+3):
                angle_temp = changedegree(angle_temp+minangle)
                x_temp = x_temp+t*bullet_speed*math.cos(math.radians(angle_temp))
                y_temp = y_temp+t*bullet_speed*math.sin(math.radians(angle_temp))
                if abs(angle_temp)<minangle:
                    x_up = x_temp
                    y_up = y_temp
                if abs(angle_temp +90)<minangle:
                    x_right = x_temp
                    y_right = y_temp
                if abs(angle_temp -90)<minangle:
                    x_left = x_temp
                    y_left = y_temp
                if (abs(angle_temp -180)<minangle)or (abs(angle_temp +180)<minangle):
                    x_down = x_temp
                    y_down = y_temp
            oa = (x_right+x_left)/2
            ob = (y_up+y_down)/2
            lena = (x_right-x_left)/2
            lenb = (y_up-y_down)/2
            lenc = (aim_x-oa)*(aim_x-oa)/(lena*lena)+(aim_y-ob)*(aim_y-ob)/(lenb*lenb)
            if lenc >1.71:
                angle = angle1
            else :
                angle = bullet_angle
            
    else :
        if abs(j2)<2*minangle:
            angle = sita
        else :
            
            angle_temp=bullet_angle
            x_temp=bullet_x
            y_temp=bullet_y
            for i in range(0,360/minangle+3):
                angle_temp = changedegree(angle_temp-minangle)
                x_temp = x_temp+t*bullet_speed*math.cos(math.radians(angle_temp))
                y_temp = y_temp+t*bullet_speed*math.sin(math.radians(angle_temp))
                if abs(angle_temp)<minangle:
                    x_up = x_temp
                    y_up = y_temp
                if abs(angle_temp +90)<minangle:
                    x_right = x_temp
                    y_right = y_temp
                if abs(angle_temp -90)<minangle:
                    x_left = x_temp
                    y_left = y_temp
                if (abs(angle_temp -180)<minangle)or (abs(angle_temp +180)<minangle):
                    x_down = x_temp
                    y_down = y_temp
            oa = (x_right+x_left)/2
            ob = (y_up+y_down)/2
            lena = (x_right-x_left)/2
            lenb = (y_up-y_down)/2
            lenc = (aim_x-oa)*(aim_x-oa)/(lena*lena)+(aim_y-ob)*(aim_y-ob)/(lenb*lenb)
            if lenc >1.71:
                angle = angle2
            else :
                angle = bullet_angle
           


    x1 = t*bullet_speed*math.cos(math.radians(angle))
    y1 = t*bullet_speed*math.sin(math.radians(angle))
    nx = 0
    ny = 0
    nx = bullet_x + x1
    ny = bullet_y + y1
    print "%f\t%f\t%f"%(nx,ny,angle)
    return (nx,ny,angle)
a = random.uniform(-40,40)
b = random.uniform(-40,40)
c = random.uniform(-180,180)

a1 = random.uniform(-40,40)
b1 = random.uniform(-40,40)
c1 = random.uniform(-180,180)


while (abs(a-a1)>0.3 or abs(b-b1)>0.3):
    (a,b,c)=func(a,b,c,5,a1,b1,c1,0,0.1)   

    
    

    
