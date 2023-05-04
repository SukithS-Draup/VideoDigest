import cv2
import os

def create_video():
    
    file_path = './output.avi'
    if os.path.isfile(file_path):
        
        video = cv2.VideoCapture("./output.avi")

        # Get video codec information and frame size
        fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        frame_size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        # Open image file
        img = cv2.imread("./frame.jpg")
        # Resize image to match video frame size
        # Open video writer and write video frames
        writer = cv2.VideoWriter("./output.avi", fourcc, fps, frame_size)
        while True:
            ret, frame = video.read()
            if not ret:
                break
            writer.write(frame)

        # Write the image as the last frame in the video
        writer.write(img)

        # Release resources
        video.release()
    else:
        # Open the JPEG image
        img = cv2.imread('./frame.jpg')

        # Create a VideoWriter object to write the frames to a video file
        output_file = 'output.avi'
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = 25.0
        frame_size = (img.shape[1], img.shape[0])
        writer = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

        # Add the image to the video as a frame
        writer.write(img)

    # Release the VideoWriter object and close the output file
    writer.release()
    return
