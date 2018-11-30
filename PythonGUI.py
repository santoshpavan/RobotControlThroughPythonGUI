import pygame ,os
import serial

ser=serial.Serial('com5',9600)

pygame.init()
screen = pygame.display.set_mode((1300,600))
pygame.display.set_caption('TEST')

w = (0,255,255)

pygame.draw.rect(screen,w,(600,50,100,100)) #front
xfmin=600
yfmin=50
xfmax=700
yfmax=150
pygame.draw.rect(screen,w,(200,225,100,100)) #left
xlmin=200
ylmin=225
xlmax=300
ylmax=325
pygame.draw.rect(screen,w,(600,450,100,100)) #back
xbmin=600
ybmin=450
xbmax=700
ybmax=550
pygame.draw.rect(screen,w,(1000,225,100,100)) #right
xrmin=1000
yrmin=225
xrmax=1100
yrmax=325
pygame.draw.rect(screen,w,(600,225,100,100))  #stop
xsmin=600
ysmin=225
xsmax=700
ysmax=325

write=pygame.font.SysFont("monospace",20)
label1=write.render("FRONT",1,(0,255,0))
screen.blit(label1,(620,70))

label2=write.render("LEFT",1,(255,255,0))
screen.blit(label2,(220,245))

label3=write.render("BACK",1,(0,255,0))
screen.blit(label3,(620,470))

label4=write.render("RIGHT",1,(255,255,0))
screen.blit(label4,(1020,245))

label5=write.render("STOP",1,(255,0,0))
screen.blit(label5,(620,245))

i=1
while(i):
    event=pygame.event.poll() #get events from the pygame
    
	  if event.type==pygame.MOUSEBUTTONDOWN:  #if the mouse button is clicked
        x=pygame.mouse.get_pos()[0]
        y=pygame.mouse.get_pos()[1]
        
        if x>xfmin and x<xfmax and y>yfmin and y<yfmax:
            ser.write("f") #sending a character 'f' through serial communication to MC
        if x>xrmin and x<xrmax and y>yrmin and y<yrmax:
            ser.write("r")
        if x>xlmin and x<xlmax and y>ylmin and y<ylmax:
            ser.write("l")
        if x>xbmin and x<xbmax and y>ybmin and y<ybmax:
            ser.write("b")
        if x>xsmin and x<xsmax and y>ysmin and y<ysmax:
            ser.write("s")
    
	  if event.type==pygame.QUIT: #if the GUI program is quit
        i=0
    pygame.display.update() #update the changes in each iteration
pygame.quit() #quit the program