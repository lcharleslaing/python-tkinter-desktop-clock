from setuptools import setup, find_packages

setup(
    name="mypcclock",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "tkinter",
        "configparser",
    ],
    entry_points={
        "console_scripts": [
            "mypcclock=mypcclock.__main__:main",
        ],
    },
)
