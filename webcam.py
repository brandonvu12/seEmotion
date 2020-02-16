import numpy as np
import cv2
import main
import alg
import time

def web():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    for i in range(30):
        cap.read()
    ret,frame = cap.read() # return a single frame in variable `frame`

    num_vals = main.trait(cv2.imencode('.jpg', frame)[1].tostring())
    if num_vals == None:
        num_vals = (0,0,0,0)
    cap.release()
    return alg.confused(num_vals)

# while(True):
#cv2.imshow('img1',frame) #display the captured image
#k = cv2.waitKey(0)
# time.sleep(5000)
    # if k == 27:
        # cv2.destroyAllWindows()
        # break
#     if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
#         cv2.imwrite('images/c1.png',frame)
#         cv2.destroyAllWindows()
#         break
#
