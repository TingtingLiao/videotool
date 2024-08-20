import cv2 
from videotool.io import load_mp4, export_gif


import coloredlogs, logging 
logger = logging.getLogger(__name__) 
coloredlogs.install(level='DEBUG', logger=logger) 


# python main.py /home/tingting/Videos/Screencasts/expcontrol.webm -s 0.5 -i 2 -o /home/tingting/Videos/Screencasts/expcontrol.gif
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("video_path", type=str, help="path to input video")
    parser.add_argument('-s', "--scale", type=float, default=1, help="path to input video")
    parser.add_argument('-i', "--interval", type=int, default=1, help="select frame intervel")
    parser.add_argument('-o', "--output", type=str, help="path to save video")
    opt, extras = parser.parse_known_args() 
 
    logger.debug('loading video...')
    frames = load_mp4(opt.video_path)

    if opt.interval > 1:
        frames = frames[::opt.interval]

    if not opt.scale == 1:
        logger.debug('resizing video...')
        w, h = frames[0].shape[:2]
        w, h = int(w * opt.scale), int(h * opt.scale)
        frames = [cv2.resize(f, (h, w)) for f in frames]

    logger.debug('exporting video...')
    export_gif(frames, opt.output)
    
    logger.debug('done!')