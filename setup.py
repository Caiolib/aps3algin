from setuptools import setup, find_packages

import os

MODULE_STUB = 'aps4'

def find_subdir(start_dir):
    # Get the list of all subdirectories starting at the given path
    subdirectories = [x[0] for x in os.walk(start_dir)]
    subdirectories = [x.split('/',1)[-1]+'/*' for x in subdirectories]
    return subdirectories

# Adiciona todos os arquivos encontrados ao package_data
setup(
    name="aps4",
    version="0.1.0",
    description="Cubo",
    author="Caio Frigerio",
    author_email="caioliberal@gmail.com",
    url="https://github.com/Caiolib/aps4",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'aps4': ['contas.py', *find_subdir(f'{MODULE_STUB}/assets')], 
    },
    install_requires=[
        "numpy==2.1.2",
        "pygame==2.6.1"

    ],
    entry_points={
        'console_scripts': [
            'aps4=aps4.app:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)

