from setuptools import setup, find_packages


setup(
    name="iot",
    version="0.1.2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"web": ["web/templates/*"]},
    scripts=["web/web.py"],
    description="IOT",
    install_requires=[
        "bottle",
        "requests"]
) 
