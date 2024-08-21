from setuptools import setup, find_packages

setup(
    name='videotool',
    version='0.0.1',
    description='video processing tools', 
    packages=find_packages(),
    install_requires=[ 
        'numpy',
        'tqdm', 
        'cv2',  
    ],
)