from setuptools import setup, find_packages
setup(
    name='django-static-sites',
    version='0.0.8',
    packages=find_packages(),
    package_data={'staticsites': ['templates/*/*-tpl', 'templates/*/*/*-tpl']},
    include_package_data=True
)
