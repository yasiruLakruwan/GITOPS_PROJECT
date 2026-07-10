from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Smart Manufacturing Machine Efficiency",
    version="1.0.0",
    author="Yasiru Lakruwan",
    install_requires=requirements,
    packages=find_packages()
)