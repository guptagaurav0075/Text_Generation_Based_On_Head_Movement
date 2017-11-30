import cv2
import numpy as np
import math

position = np.empty(shape=(0,0));

# define font and text color
font = cv2.FONT_HERSHEY_SIMPLEX

# path to face cascde
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# define movement threshodls
max_head_movement = 20
movement_threshold = 50
gesture_threshold = 175

# find the face in the image
face_found = False
frame_num = 0

# capture source video
cap = cv2.VideoCapture(0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
ret, frame = cap.read()
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



# params for ShiTomasi corner detection
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)

# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


# dinstance function
def distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)



# function to get coordinates
def get_coords(p1):
    try:
        return int(p1[0][0][0]), int(p1[0][0][1])
    except:
        return int(p1[0][0]), int(p1[0][1])


def getFaceCenter(frame):
    global face_found;
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
    pos = np.array([0,0]);
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_center = x + w / 2, y + h / 2
        pos = np.array([[face_center]], np.float32)
        face_found = True
    return pos

def waitFrames(message, waitCount):
    global face_found, position;
    reinitialize();
    count =0;
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        pos1=getFaceCenter(frame);
        if (face_found and count>waitCount):
            break;
        elif(face_found and count<waitCount+1):
            count+=1

        cv2.putText(frame,  message, (50, 50), font, 1.2, (0, 0, 255), 3)
        cv2.imshow('image', frame)
        cv2.waitKey(1)

def monitorHeadMotion(message):
    global face_found, frame_num, position;
    # cv2.resizeWindow('image', 600, 600)
    reinitialize()
    count =0;
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        pos1 = getFaceCenter(frame);
        if (face_found):
            position = np.append(position, pos1);
            count+=1;
            face_found = False;
            if count ==2: # To check if two consecutive times the faces are found
                break;
        else:
            count=0;
            position = [];
        cv2.putText(frame, message, (50, 50), font, 1.2, (0, 0, 255), 3)
        cv2.imshow('image', frame)
        k = cv2.waitKey(15) & 0xFF

        if (k == 27 or k == ord('q') or k == ord('Q')):  # ESC
            # this argument helps in quiting the application
            setExit = True;
            cv2.destroyAllWindows()
            exit(0)

    return getAverageFacePosition(position, count)

def reinitialize():
    global position;
    position = np.empty(shape=(0, 0));


def findInitialFaceWithMessage(message):
    global face_found, frame_num, position;
    reinitialize();
    count =0;
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        pos1=getFaceCenter(frame);
        if (face_found and count>20):
            # pos1 = getFaceCenter(frame);
            # print pos1;
            position = np.append(position, pos1);
            count+=1;
            face_found = False;
            if count ==50: # To check if two consecutive times the faces are found
                break;
        elif(face_found and count<21):
            count+=1
        # print count

        cv2.putText(frame,  message, (50, 50), font, 1.2, (0, 0, 255), 3)
        cv2.imshow('image', frame)
        k = cv2.waitKey(15) & 0xFF

        if (k == 27 or k == ord('q') or k == ord('Q')):  # ESC
            # this argument helps in quiting the application
            setExit = True;
            cv2.destroyAllWindows()
            exit(0)
    # print position
    return getAverageFacePosition(position, count-21)


def getAverageFacePosition(position, count):
    return position.reshape(count,2).mean(0).reshape(1,1,2)
