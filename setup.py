from setuptools import setup, find_packages


setup(
    name="iot",
    version="0.1.2",
    description="IOT",
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={
        "web": ["templates/*", "static/*",]
    },
    install_requires=[
        "bottle",
        "requests"]
)
