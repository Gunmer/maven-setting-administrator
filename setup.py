from setuptools import setup

setup(
    name='msm',
    version='0.0.1',
    description='Maven settings manager',
    url='https://github.com/Gunmer/maven-setting-manager',
    author='Gunmer',
    author_email='csosaur@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=['src.msm'],
    scripts=['bin/msm'],
    entry_points={'console_scripts': ['src=src.msn.command_line:main']}
)
