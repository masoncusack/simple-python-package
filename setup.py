from setuptools import find_packages, setup

with open("requirements.txt", "r") as f:
    REQUIRES=[
        line.strip() for line in f.readlines()
    ]

setup(
    name="package",
    version="0.0.1",
    author="Package Author",
    author_email="someone@email.com",
    description="A great description of this package.",
    keywords="something cool",
    url="https://github.com/masoncusack/simple-python-package",
    install_requires=REQUIRES,
    packages=find_packages()
)
