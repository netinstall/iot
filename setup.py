from setuptools import setup, find_packages
setup(
    name='django-static-sites',
    version='0.0.8',

    package_data={
        "": ["*.txt"],
        "mypkg": ["data/*.dat"],
    }
)
