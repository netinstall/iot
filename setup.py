from setuptools import setup, find_packages
setup(
    name="mypkg",
    version="0.1",
    packages=find_packages("src"),  # include all packages under src
    package_dir={"": "src"},   # tell distutils packages are under src

    package_data={
        # If any package contains *.txt files, include them:
        "": ["*.txt"],
        # And include any *.dat files found in the "data" subdirectory
        # of the "mypkg" package, also:
        "mypkg": ["data/*.dat"],
    }
)
