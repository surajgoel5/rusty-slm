from setuptools import setup, find_packages

setup(
    name="rusty_slm",
    version="2.0.0",
    url="https://github.com/surajgoel5/rusty-slm",
    author="Max Tyler, Suraj Goel",
    author_email="maxastyler@gmail.com, goel.suraj5@gmail.com",
    description="Forked from Max Tyler's - Functions to interact with an SLM, imporved to use lower versions of python and backward compatibility",
    packages=find_packages(include=["rusty_slm"]),
    include_package_data=True,
    install_requires=["grpcio>=1.15.0","importlib-resources","protobuf"],
    package_data={'rusty-slm': ['binaries/*']},
)
