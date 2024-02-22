from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="simple_greeter",
    version="0.1.0",
    author="Zack Ward",
    author_email="ZackWard.cs@gmail.com",
    description="A simple package to greet people",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZachariahWard/simple_greeter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)