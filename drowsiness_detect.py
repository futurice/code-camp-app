'''This script detects if a person is drowsy or not,using dlib and eye aspect ratio
calculations. Uses webcam video feed as input.'''

#Import necessary libraries
from scipy.spatial import distance
from imutils import face_utils
import numpy as np
import time
import dlib
import cv2
import os

#Minimum threshold of eye aspect ratio below which alarm is triggerd
EYE_ASPECT_RATIO_THRESHOLD = 0.3

#Minimum consecutive frames for which eye ratio is below threshold for alarm to be triggered
EYE_ASPECT_RATIO_CONSEC_FRAMES = 5

#How many images to analyze before returning not drowsy status
NUM_OF_IMAGES_IN_ONE_ANALYSIS = 10

#This function calculates and return eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A+B) / (2*C)
    return ear

#Load face detector and predictor, uses dlib shape predictor file
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#Extract indexes of facial landmarks for the left and right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

def analyze_picture(state):
    #Open the next image file
    frame = cv2.imread(state['image_name'])

    #Read each frame and flip it, and convert to grayscale
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect facial points through detector function
    faces = detector(gray, 0)

    #Detect facial points
    for face in faces:
        eye_aspect_ratio = get_eye_aspect_ratio(gray, face)

        #Detect if eye aspect ratio is less than threshold
        if (eye_aspect_ratio < EYE_ASPECT_RATIO_THRESHOLD):
            if state['drowsiness_count'] >= EYE_ASPECT_RATIO_CONSEC_FRAMES:
                return (state['drowsiness_count'] + 1, state['max_drowsiness'] + 1)
            else:
                return (state['drowsiness_count'] + 1, state['max_drowsiness'])

    return (0, state['max_drowsiness'])

def get_eye_aspect_ratio(gray, face):
    shape = predictor(gray, face)
    shape = face_utils.shape_to_np(shape)

    #Get array of coordinates of leftEye and rightEye
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]

    #Calculate aspect ratio of both eyes
    leftEyeAspectRatio = eye_aspect_ratio(leftEye)
    rightEyeAspectRatio = eye_aspect_ratio(rightEye)

    eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2

    return eyeAspectRatio

image_name_generator = (f"./images/image_{seq}.jpg" for seq in range(10000000000))

# running drowsiness counter, image counter, highest drowsiness level yet, current image
# 0 = not drowsy
# 1 = drowsy

def fresh_analyzer_state():
    return {
        'drowsiness_count': 0, 
        'image_count': 0,
        'max_drowsiness': 0,
        'image_name': ''
    }

analyzer_state = fresh_analyzer_state()

while True:
    for image_name in image_name_generator:
        print(image_name)
        # loop until next image in the sequence is found 
        while True:
            if (os.path.exists(image_name) and os.path.isfile(image_name)):
                analyzer_state['image_count'] += 1 
                analyzer_state['image_name'] = image_name
                drowsiness_count, max_drowsiness = analyze_picture(analyzer_state)
                analyzer_state['drowsiness_count'] = drowsiness_count

                if (max_drowsiness != 0):
                    if (analyzer_state['max_drowsiness'] < max_drowsiness):
                        analyzer_state['max_drowsiness'] = max_drowsiness
                        with open('./images/result.txt', 'w') as f:
                            print("T")
                            f.write("t")
                # subject was not drowsy
                elif (analyzer_state['image_count'] == NUM_OF_IMAGES_IN_ONE_ANALYSIS):
                    if (analyzer_state['max_drowsiness'] == 0):
                        with open('./images/result.txt', 'w') as f:
                            print("F")
                            f.write("f")
                    analyzer_state = fresh_analyzer_state()

                print("remove...")
                #os.remove(image_name)
                break
