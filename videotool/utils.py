import cv2 
import numpy as np 


def hstack_videos(video_list):
    '''
    hstack multiple videos into a single video
    
    Args:
        video_list: list of video_frames 
    ''' 
    stacked_frames = []
    for frames in zip(*video_list):
        stacked_frames.append(np.hstack(frames))
    return stacked_frames


def vstack_videos(video_list):
    '''
    vstack multiple videos into a single video
    
    Args:
        video_list: list of video_frames 
    ''' 
    stacked_frames = []
    for frames in zip(*video_list):
        stacked_frames.append(np.vstack(frames))
    return stacked_frames

def resize_video(frame_list, size):
    '''
    Resize a list of video frames to a specified size while preserving aspect ratio
    if one of the dimensions is set to <= 0.

    Args:
        frame_list (list of np.ndarray): List of video frames (HWC format).
        size (tuple): (height, width). If one dimension <= 0, it will be computed to preserve aspect ratio.

    Returns:
        list of np.ndarray: Resized video frames.
    '''
    h, w = size
    hh, ww = frame_list[0].shape[:2]

    if h <= 0 and w > 0:
        h = int(w / ww * hh)
    elif h > 0 and w <= 0:
        w = int(h / hh * ww)
    elif h <= 0 and w <= 0:
        raise ValueError("At least one of height or width must be > 0.")
    # else: both h and w are given and valid

    frame_list = [cv2.resize(f, (w, h)) for f in frame_list]
    return frame_list
