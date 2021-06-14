from setuptools import setup, find_packages
setup(
    name='django-static-sites',
    version='0.0.8',
    packages=find_packages("src"),  # include all packages under src
    package_dir={"": "src"},   # tell distutils packages are under src

    package_data={
        "": ["*.txt"],
        "mypkg": ["data/*.dat"],
    }
)
