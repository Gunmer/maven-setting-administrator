from setuptools import *

from msa.utils.config import Config

setup(
    name='msa',
    version=Config.version,
    description='Maven settings administrator',
    url='https://github.com/Gunmer/maven-setting-administrator.git',
    author='Gunmer',
    author_email='csosaur@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    scripts=['bin/msa'],
    entry_points={'console_scripts': ['src=msn.command_line:main']},
    test_suite='test',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
