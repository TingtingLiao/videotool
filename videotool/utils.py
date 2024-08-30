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
