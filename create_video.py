import cv2
import os

def create_video(img_folder,file_name):
    
    file_path = './static/video/'+file_name
    # Folder containing the JPG images

    # Sort the images by name
    img_names = sorted(os.listdir(img_folder))

    # Get the first image to set the frame size
    first_img = cv2.imread(os.path.join(img_folder, img_names[0]))
    height, width, _ = first_img.shape

    # Create a video writer object
    out = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'avc1'), 50, (width, height))

    # Iterate over the images and add them to the video
    for img_name in img_names:
        img_path = os.path.join(img_folder, img_name)
        img = cv2.imread(img_path)
        out.write(img)

    # Release the video writer object
    out.release()
    return

