from setuptools import setup, find_packages

setup(
    name="cybertemp-wrapper-py",
    version="1.0.0",
    description="A Python wrapper for the CyberTemp email API.",
    author="Never",
    url="https://github.com/raz461/cybertemp-wrapper-py",
    project_urls={
        "Source": "https://github.com/raz461/cybertemp-wrapper-py",
        "Bug Tracker": "https://github.com/raz461/cybertemp-wrapper-py/issues",
    },
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    python_requires=">=3.10"
)
