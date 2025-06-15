import cv2
import mediapipe as mp
mp_hand=mp.solutions.hands
hand=mp_hand.Hands()
mp_draw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)

while True:
    id_8 = None
    id_4 = None
    x1 = x2 = y1 = y2 = None
    distance = distance_in_cm = distance_in_inch = None
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=hand.process(frame_rgb)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id , lm in enumerate (handLms.landmark):
                h,w,c=frame.shape
                cx=int(lm.x*w)
                cy=int(lm.y*h)
                if id == 8:
                    id_8 = cx , cy
                    x1,y1=id_8
                if id == 4:
                    id_4 = cx, cy
                
                    x2,y2=id_4
                if x1 is not None and x2 is not None and y1 is not None and y2 is not None:
                    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
                    distance_in_inches = distance / 96
                    distance_in_cm = distance_in_inches * 2.54
                    distance_in_inches = distance / 96
                    distance_in_cm = distance_in_inches * 2.54
                    distance_in_cm = int(distance_in_cm)
                    distance_in_inches = int(distance_in_inches)


                print(f"ID:{id},x:{cx},y:{cy}")
                if id_8 is not None and id_4 is not None:
            
                    cv2.circle(frame,(id_8),10,(255,0,255),cv2.FILLED)
                    cv2.circle(frame,(id_4),10,(255,0,255),cv2.FILLED)
                    cv2.line(frame,id_8,id_4,(255,0,0),5)
                   
                    cv2.putText(frame,f'distance:{distance_in_cm}',(20,70),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,0),4)
            mp_draw.draw_landmarks(frame,handLms,mp_hand.HAND_CONNECTIONS)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()