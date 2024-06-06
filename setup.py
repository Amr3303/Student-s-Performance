from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requierments(file_path:str)->List[str]:
    """this function will return a list of requirements

    Args:
        file_path (str): path to the requirements.txt file

    Returns:
        List[str]: a list of all the requirements
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements= [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name= "Student's Performance",
    version= "0.1",
    author="Amr",
    author_email="amrkhaled3303@gmail.com",
    packages= find_packages(),
    install_requiers = get_requierments("requirements.txt"),
    
)