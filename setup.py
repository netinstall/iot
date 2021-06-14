from setuptools import setup, find_packages
setup(
    name='iot',
    version='0.0.8',
    packages=find_packages(),
    package_data={'web': ['static']},
    include_package_data=True,
    license='GNU GENERAL PUBLIC LICENSE',
    description='An easy to use Django app to make static site.',
)
