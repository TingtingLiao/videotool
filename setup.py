from setuptools import setup, find_packages

setup(
    name='videotool',
    version='0.0.1',
    description='video processing tools', 
    packages=find_packages(),
    entry_points={
        # CLI tools
        'console_scripts': [
            'vtl = main:main', 
        ],
    },
    install_requires=[ 
        'numpy',
        'tqdm', 
        'opencv-python',  
        'rich', 
        'imageio',
        'imageio-ffmpeg'
    ],
)