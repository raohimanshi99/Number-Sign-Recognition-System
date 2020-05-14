import cv2
import os

if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/test")
    os.makedirs("data/train")
    os.makedirs('data/test/0')
    os.makedirs('data/train/0')
    os.makedirs('data/train/1')
    os.makedirs('data/test/1')
    os.makedirs('data/train/2')
    os.makedirs('data/test/2')
    os.makedirs('data/train/3')
    os.makedirs('data/test/3')
    os.makedirs('data/train/4')
    os.makedirs('data/test/4')
    os.makedirs('data/train/5')
    os.makedirs('data/test/5')
    os.makedirs('data/train/6')
    os.makedirs('data/test/6')
    os.makedirs('data/train/7')
    os.makedirs('data/test/7')
    os.makedirs('data/train/8')
    os.makedirs('data/test/8')
    os.makedirs('data/train/9')
    os.makedirs('data/test/9')
#    os.makedirs('data/test/y')
#    os.makedirs('data/train/y')
    
cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,680)

directory = 'data/train/'
mode = 'train'

while True:
    b,frame = cap.read()
    frame = cv2.flip(frame,1)
    count = {
                'zero'  : len(os.listdir(directory+'/0')),
                'one'   : len(os.listdir(directory+'/1')),
                'two'   : len(os.listdir(directory+'/2')),
                'three' : len(os.listdir(directory+'/3')),
                'four'  : len(os.listdir(directory+'/4')),
                'five'  : len(os.listdir(directory+'/5')),
                'six'   : len(os.listdir(directory+'/6')),
                'seven' : len(os.listdir(directory+'/7')),
                'eight' : len(os.listdir(directory+'/8')),
                'nine'  : len(os.listdir(directory+'/9')),
#                'yra'   : len(os.listdir(directory+'/y'))
            }
    
    
    
    cv2.rectangle(frame,(10,0),(300,475),(200,150,100),cv2.FILLED)
    cv2.putText(frame,"Data     Images",(20,25),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    cv2.putText(frame,'0 -   '+ str(count['zero']),(48,75),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'1 -   '+str(count['one']),(48,115),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'2 -   '+str(count['two']),(48,155),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'3 -   '+str(count['three']),(48,195),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'4 -   '+str(count['four']),(48,235),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'5 -   '+str(count['five']),(48,275),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'6 -   '+str(count['six']),(48,315),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'7 -   '+str(count['seven']),(48,355),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'8 -   '+str(count['eight']),(48,395),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    cv2.putText(frame,'9 -   '+str(count['nine']),(48,435),cv2.FONT_HERSHEY_DUPLEX,1.25,(255,255,255),1)
    #cv2.putText(frame,'Cool - '+str(count['yra']),(48,305),cv2.FONT_HERSHEY_DUPLEX,0.75,(55,55,55),1)
    
    cv2.putText(frame,"Module 1:",(20,550),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(255,255,255),1)
    cv2.putText(frame,"Preparation Of DataSets ",(20,600),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(255,255,255),1)
    
    
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    
    roi = cv2.resize(roi, (64, 64)) 
    cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    a,roi = cv2.threshold(roi,120,255,cv2.THRESH_BINARY)
    cv2.imshow("Region of interest",roi)
    
    
    cv2.imshow("MyProject",frame)
    
    interupt = cv2.waitKey(10)
    
    if interupt & 0xFF == 27:
        break
    elif interupt & 0xFF == 48:
        path = directory+'0/'+str(count['zero'])+'.jpg'
        cv2.imwrite(path,roi)
        print(path)
        
    elif interupt & 0xFF == 49:
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg',roi)
    elif interupt & 0xFF == 50:
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg',roi)
    elif interupt & 0xFF == 51:
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg',roi)
    elif interupt & 0xFF == 52:
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg',roi)
    elif interupt & 0xFF == 53:
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg',roi)
    elif interupt & 0xFF == 54:
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg',roi)
    elif interupt & 0xFF == 55:
        cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg',roi)
    elif interupt & 0xFF == 56:
        cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg',roi)
    elif interupt & 0xFF == 57:
        cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg',roi)
#    elif interupt & 0xFF == 58:
#        cv2.imwrite(directory+'y/'+str(count['yra'])+'.jpg',roi)
        
        
cap.release()
cv2.destroyAllWindows()