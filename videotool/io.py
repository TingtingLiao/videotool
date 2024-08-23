import os  
import imageio 
from PIL import Image
from rich.progress import track

import coloredlogs, logging 
logger = logging.getLogger(__name__) 
coloredlogs.install(level='DEBUG', logger=logger) 


def load_video(video_path, n_frames=-1, return_fps=False):
    reader = imageio.get_reader(video_path, "ffmpeg")
    fps = reader.get_meta_data()['fps']

    ret = []
    for idx, frame_rgb in enumerate(reader):
        if n_frames > 0 and idx >= n_frames:
            break
        ret.append(frame_rgb)

    reader.close()

    if return_fps:
        return ret, fps
    
    return ret 


def export_video(images, wfp, **kwargs):
    '''
    '''
    fps = kwargs.get('fps', 30)
    video_format = kwargs.get('format', 'mp4')  # default is mp4 format
    codec = kwargs.get('codec', 'libx264')  # default is libx264 encoding
    quality = kwargs.get('quality')  # video quality
    pixelformat = kwargs.get('pixelformat', 'yuv420p')  # video pixel format
    image_mode = kwargs.get('image_mode', 'rgb')
    macro_block_size = kwargs.get('macro_block_size', 2)
    ffmpeg_params = ['-crf', str(kwargs.get('crf', 18))]

    writer = imageio.get_writer(
        wfp, fps=fps, format=video_format,
        codec=codec, quality=quality, ffmpeg_params=ffmpeg_params, pixelformat=pixelformat, macro_block_size=macro_block_size
    )
 
    for i in track(range(len(images)), description='Writing', transient=True):
        if image_mode.lower() == 'bgr':
            writer.append_data(images[i][..., ::-1])
        else:
            writer.append_data(images[i])

    writer.close()



def export_gif(frames, save_path, loop=0):
    images = [Image.fromarray(f[..., ::-1]) for f in frames]
    images[0].save(save_path, save_all=True, append_images=images[1:], loop=loop, duration=100)
 