import os 
import cv2
import face_recognition
import argparse

def match_target_face(target_img_path, storage_folder='/home/arthurlin/workspace/Projects/face_recognition/storage', tolerance=0.3):
    """
    Compare the targeted face image and the images stored in database
    Args:
        target_img_path (str): the path of targeted face 
        storage_folder (str): the database of cropped images
        tolerance (float): the threshold of similarity (the smaller, the stricker)
    Return:
        List[dict]: including the infomation of matched images 
    """

    target_img = face_recognition.load_image_file(target_img_path)
    target_encodings = face_recognition.face_encodings(target_img)
    
    if len(target_encodings) == 0:
        return [] # can not find the faces 

    target_encoding = target_encodings[0]
    matched_results = []

    for root, _, files in os.walk(storage_folder):
        for file in files:
            if not file.endswith(('.jpg', '.png')):
                continue 
            
            storage_path = os.path.join(root, file)
            storage_img = cv2.imread(storage_path)
            storage_img = cv2.cvtColor(storage_img, cv2.COLOR_BGR2RGB)

            encodings = face_recognition.face_encodings(storage_img)
            if not encodings:
                continue 

            face_distance = face_recognition.face_distance([target_encoding], encodings[0])[0]
            if face_distance <= tolerance:
                matched_results.append({
                    "matched_file": storage_path,
                    "distance": float(face_distance)
                })
    return matched_results
