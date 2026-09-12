from setuptools import setup, find_packages

setup(
    name='CodeGuardianPro',
    version='1.0.0',
    description='Visual Secret & Vulnerability Context Analyzer',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'tkinter',
        'customtkinter'
    ],
    entry_points={
        'console_scripts': [
            'codeguardianpro=gui_app:main'
        ]
    }
)