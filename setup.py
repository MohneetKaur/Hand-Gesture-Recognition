from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="HandGestureRecognition",
    version="0.0.1",
    author="Mohneet Kaur Sandhu",
    author_email="mohneetkaursandhu@gmail.com",
    install_requires=get_requirements(r"C:\\Users\\HP\\Documents\\projects\\Hand Gesture Recognition System\\smart_tv_gesture_recognition\\requirements.txt"),
    packages=find_packages(include=["components", "models", "pipeline", "realtime", "cloud_storage"])
)