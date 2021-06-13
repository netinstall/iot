from setuptools import setup


setup(
    name="iot",
    version="0.1.2",
    packages=find_packages("."),
    package_dir={"": "."},
    scripts=["web/web.py"],
    description="IOT",
    install_requires=[
        "bottle",
        "requests"],
    package_data={"": ["web/templates/*"]}
) 
