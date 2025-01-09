'''
The setup.py file is an essential part of packaging and distributing Python projects. It is used by setuptools
(or distutils in older python versions) to define the configuration of your project, 
such as its metadata, dependencies and more.

'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This funciton will return list of requirements
    """

    requirement_lst:List[str]=[]  # es ka mtlb hai ki requirement_lst variable initialise kra and uske andr list of strings honge and equal ke baad [] means ki uska return type bhi string he hoga
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines= file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip() # use to remove every empty spaces 
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':  # es code ka mtlb h ki agar kisi line me -e . mila then append it and # required/ important to triggering setup.py file and to automatically build all the files
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")


    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ishan Pandey",
    author_email="pandeyishan44@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

                






