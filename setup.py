from setuptools import setup, find_packages
setup(
    name='django-static-sites',
    version='0.0.8',
    packages=find_packages(),
    package_data={'staticsites': ['templates/*/*-tpl', 'templates/*/*/*-tpl']},
    include_package_data=True,
    license='GNU GENERAL PUBLIC LICENSE',
    description='An easy to use Django app to make static site.',
    entry_points={
        'console_scripts': ['django-static-admin=staticsites.management:execute_from_command_line'],
    },
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/ciotto/django-static-sites',
    author='Christian Bianciotto',
    author_email='info@ci8.it',
    package_dir={'django-static-sites': 'lib/django-static-sites'},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
