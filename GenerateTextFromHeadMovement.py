import numpy as np;
import math;
import cv2;
import GetHeadMotions as ghm;
from numpy import linalg as la;

AVERAGE_LEFT = np.empty(shape=(1,2)); # Used to find the average left position of the head
AVERAGE_RIGHT = np.empty(shape=(1,2)); # Used to find the average right position of the head
AVERAGE_TOP = np.empty(shape=(1,2)); # Used to find the average top position of the head
AVERAGE_DOWN = np.empty(shape=(1,2)); # Used to find the average down position of the head
AVERAGE_NORMAL = np.empty(shape=(1,2)) #Used to find the average normal position of the head


# AVERAGE_LEFT = np.array([[ 466.6 ,284.6]])
# AVERAGE_RIGHT = np.array([[ 620.7, 290.1]])
# AVERAGE_TOP = [[ 598. ,  258.9]]
# AVERAGE_DOWN = np.array([[ 617.7  ,324.6]])
# AVERAGE_NORMAL = np.array([[ 564.4 , 276.2]])

POSITIONS = np.array([AVERAGE_NORMAL, AVERAGE_LEFT, AVERAGE_RIGHT, AVERAGE_DOWN, AVERAGE_TOP]);
MESSAGE_POSITION = ["Normal Position", "Move Head Towards Left", "Move Head Towards Right", "Move Head Towards Down", "Move Head Towards Top"];
TEXT_CHARACTERS = {"Left":
                       {
                           "Left":"A",
                           "Top":"B",
                           "Down":"C",
                           "Right":"D"
                       },
                    "Top":
                       {
                           "Left":"E",
                           "Top":"F",
                           "Down":"G",
                           "Right":"H"
                       },
                    "Down":
                       {
                           "Left":"I",
                           "Top":"J",
                           "Down":"K",
                           "Right":"L"
                       },
                    "Right":
                       {
                           "Left":"M",
                           "Top":"N",
                           "Down":"O",
                           "Right":"P"
                       }
                   }

POSITION_DESCRIPTION = ["Normal", "Left", "Right", "Down", "Top"];

CURRENT_POSITION = np.empty(shape=(1,2))
# CURRENT_POSITION = np.array([[[ 598.5 ,200.5]]])
MESSAGE = "Normal"
last_Position = MESSAGE

def calEigenDistance():
    global CURRENT_POSITION, POSITIONS;
    eid = np.empty(shape=(5));
    for i in range(len(POSITIONS)):
        resultantVector = np.array([CURRENT_POSITION.reshape(2)[0]-POSITIONS[i].reshape(2)[0],CURRENT_POSITION.reshape(2)[1]-POSITIONS[i].reshape(2)[1]])
        eid[i] = (la.norm(resultantVector,2))
        # print eid[i]
    # print POSITION_DESCRIPTION[np.argmin(eid)]
    return POSITION_DESCRIPTION[np.argmin(eid)]

def readInitialMovements():
    global POSITIONS
    for i in range(len(POSITIONS)):
        POSITIONS[i] = ghm.findInitialFaceWithMessage(message=MESSAGE_POSITION[i])
        print "Average Position of ", POSITION_DESCRIPTION[i], " is : ", POSITIONS[i]

readInitialMovements()


# while True:
#     # print "Hello"
#     CURRENT_POSITION=ghm.monitorHeadMotion(message=MESSAGE)
#     print CURRENT_POSITION
#     MESSAGE = calEigenDistance();

def motion():
    global CURRENT_POSITION, MESSAGE;
    CURRENT_POSITION = ghm.monitorHeadMotion(message=MESSAGE)
    # print CURRENT_POSITION
    MESSAGE = calEigenDistance();
    # return MESSAGE;

def motion1(msg):
    global CURRENT_POSITION, MESSAGE;
    CURRENT_POSITION = ghm.monitorHeadMotion(message=msg)
    # print CURRENT_POSITION
    MESSAGE = calEigenDistance();
    # return MESSAGE;

def changeInMovement():
    global MESSAGE, last_Position;
    if(MESSAGE== last_Position):
        # print "No change"
        return False;
    else:
        last_Position = MESSAGE
        # print "Change Detected"
        return True;

def show_image(imageName):
    imageName = "Images/" + imageName+".jpg";
    img2 = cv2.imread(imageName)
    cv2.imshow("window2", img2)

def readTextCharacters():
    global MESSAGE
    waitForNormal()
    while True:
        motion();
        show_image("Normal")
        if(changeInMovement() and MESSAGE not in "Normal"):
            selection(TEXT_CHARACTERS[MESSAGE])
            waitForNormal()


def waitForNormal():
    global MESSAGE
    while True:
        motion1("Wait For Normal")
        if(MESSAGE in "Normal"):
            break;
def selection(SelectedText):
    global MESSAGE
    # ghm.waitFrames(MESSAGE, 10)
    show_image(MESSAGE)
    waitForNormal()
    while True:
        motion()
        if(changeInMovement() and MESSAGE not in "Normal"):
                print SelectedText[MESSAGE]
                break;

readTextCharacters()