from setuptools import setup

from msa import config

setup(
    name='msa',
    version=config.msa_version,
    description='Maven settings administrator',
    url='https://github.com/Gunmer/maven-setting-administrator.git',
    author='Gunmer',
    author_email='csosaur@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=['msa', 'msa.action', 'msa.util'],
    scripts=['bin/msa'],
    entry_points={'console_scripts': ['src=msn.command_line:main']}
)
