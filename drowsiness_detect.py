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
EYE_ASPECT_RATIO_THRESHOLDS = [(0.15, 'high_drowsiness'), (0.25, 'some_drowsiness'), (0.35, 'low_drowsiness')]

#Minimum consecutive frames for which eye ratio is below threshold for alarm to be triggered
EYE_ASPECT_RATIO_REQUIRED_FRAMES = 5

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

def analyze_picture(image):
    #Read each frame and flip it, and convert to grayscale
    frame = cv2.flip(image, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect facial points through detector function
    faces = detector(gray, 0)

    #Detect facial points
    for face in faces:
        eye_aspect_ratio = get_eye_aspect_ratio(gray, face)

        #Detect if eye aspect ratio is less than some threshold
        for threshold, level in EYE_ASPECT_RATIO_THRESHOLDS:
            if (eye_aspect_ratio < threshold):
                return level

    return None

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

def get_next_image(image_name):
    while True:
        if (os.path.exists(image_name)):
            if (os.path.isfile(image_name)):
                img = cv2.imread(image_name)
                if img is None:
                    time.sleep(0.1)
                else:
                    return img

def get_final_drowsiness_level(drowsiness_counts):
    l = lambda key: drowsiness_counts[key] >= EYE_ASPECT_RATIO_REQUIRED_FRAMES
    filtered = list(filter(l, drowsiness_counts.keys()))
    print(filtered)
    return filtered[0] if len(filtered) > 0 else 'no_drowsiness'

def fresh_analyzer_state():
    return {
            'high_drowsiness': 0,
            'some_drowsiness': 0,
            'low_drowsiness': 0
        }

analyzer_state = fresh_analyzer_state()

image_name_generator = ((seq, f"./images/image_{seq}.jpg") for seq in range(10000000000))

while True:
    for image_num, image_name in image_name_generator:
        print(image_name)
        # waits until next image in the sequence is found
        image = get_next_image(image_name)
        drowsiness_level = analyze_picture(image)
        if (drowsiness_level == None):
            continue
        analyzer_state[drowsiness_level] += 1

        # we have analysed enough images
        if (image_num != 0 and image_num % NUM_OF_IMAGES_IN_ONE_ANALYSIS == 0):
            drowsiness_level = get_final_drowsiness_level(analyzer_state)
            with open('./images/result.txt', 'w') as f:
                print("drowsiness level:", drowsiness_level)
                f.write(drowsiness_level)
            analyzer_state = fresh_analyzer_state()

        os.remove(image_name)

