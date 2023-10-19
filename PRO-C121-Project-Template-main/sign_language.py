import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4


while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)

def countFingers(image,hand_landmarks,handNo=0):
        landmarks = hand_landmarks[handNo].landmark
        fingers=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                #accessing the landmarks by their position
                lm_list=[]
                for id ,lm in enumerate(hand_landmark.landmark):
                        lm_list.append(lm)
                        fingerTipy= landmarks[lm_list].y
                        fingerBottomy= landmarks[lm_list-2].y
                        thumbtipx = landmarks[lm_list].x
                        thumbbottomx= landmarks[lm_list-2].x
                        if lm_list!= 4:
                            if fingerTipy<fingerBottomy:
                                fingers.append(1)
                                print('finger with id', lm_list, 'is open')
                            if fingerTipy>fingerBottomy:
                                fingers.append(0)
                                print('finger with id', lm_list, 'is closed')
                        else:
                            if thumbtipx<thumbbottomx:
                                fingers.append(0)
                                print('thumb is open')
                            if thumbbottomx>thumbtipx:
                                fingers.append(1)
                                print('thumb is closed')

                



                mp_draw.draw_landmarks(img, hand_landmark,
                mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
                mp_draw.DrawingSpec((0,255,0),4,2))
    

cv2.imshow("hand tracking", img)
cv2.waitKey(1)