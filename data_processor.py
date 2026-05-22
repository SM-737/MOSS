import cv2
import numpy as np
import os

def generate_sync_data(video_path="test.mp4", output_dir="data"):
    """
    Slices a video and generates simulated neuromorphic event streams.
    Saves everything to a local 'data' folder for the dashboard to read.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    cap = cv2.VideoCapture(video_path)
    frame_idx = 0
    
    # Read the video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Resize frame to keep the online app running fast and smooth
        frame = cv2.resize(frame, (400, 300))
        
        # Save standard RGB image
        cv2.imwrite(os.path.join(output_dir, f"rgb_{frame_idx}.jpg"), frame)
        
        # Simulate an event camera tracking high-speed light changes
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        event_frame = np.zeros((300, 400, 3), dtype=np.uint8)
        
        # Green points represent increased light; Red points represent decreased light
        event_frame[laplacian > 12] = [0, 255, 0]   
        event_frame[laplacian < -12] = [255, 0, 0]  
        
        # Save the simulated asynchronous event slice
        cv2.imwrite(os.path.join(output_dir, f"event_{frame_idx}.jpg"), event_frame)
        
        frame_idx += 1
        if frame_idx >= 50: # Limit to 50 frames to keep the free hosting fast
            break
            
    cap.release()
    print(f"Success: Generated {frame_idx} synchronized sensor slices.")

if __name__ == "__main__":
    generate_sync_data()
