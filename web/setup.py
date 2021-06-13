from setuptools import setup


setup(
    name="iot",
    version="0.1.1",
    scripts=["web.py"],
    description="IOT",
    install_requires=[
        "bottle",
        "requests"],
    packages=["iot"],
    package_data={'iot': ["templates/*"]}
) 
