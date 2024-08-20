import os 
import os.path as osp 
import cv2
from PIL import Image

import coloredlogs, logging 
logger = logging.getLogger(__name__) 
coloredlogs.install(level='DEBUG', logger=logger) 


def load_mp4(video_path):
    '''
    load video frames from mp4 file
        Args:
        ----- 
        video_path: str
            path to the video file
          
        Returns:
        -----
        frames: list
    '''
    assert osp.exists(video_path), logger.error(f"video {video_path} not found!")
      
    frames = []
    cap = cv2.VideoCapture(video_path) 
 
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
  
        frames.append(frame)

    return frames 



def export_gif(frames, save_path, loop=0):
    images = [Image.fromarray(f[..., ::-1]) for f in frames]
    images[0].save(save_path, save_all=True, append_images=images[1:], loop=loop, duration=100)
 