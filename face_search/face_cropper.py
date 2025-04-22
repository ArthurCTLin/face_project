import os 
import face_recognition
import matplotlib.pyplot as plt 
import argparse

def crop_faces_and_save(filename, output_root='./storage'):
    
    """
    Args:
        filename (str): original image paths
        output_root (str): the path saving the cropped images

    Returns:
        List[str]: the paths of the cropped images
    """
    
    image = face_recognition.load_image_file(filename)
    face_locations = face_recognition.face_locations(image)

    cropped_paths = []

    for i, box in enumerate(face_locations):
        folder_name = os.path.splitext(os.path.basename(filename))[0]
        output_dir = os.path.join(output_root, folder_name)
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f'{folder_name}__{i}.jpg')
        cropped_face = image[box[0]:box[2], box[3]:box[1], :]
        plt.imsave(output_path, cropped_face)
        cropped_paths.append(output_path)

    return cropped_paths
