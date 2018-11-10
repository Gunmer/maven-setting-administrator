from setuptools import setup

setup(
    name='msm',
    version='1.0.0',
    description='Maven settings manager',
    url='https://github.com/Gunmer/maven-setting-manager',
    author='Gunmer',
    author_email='csosaur@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=['msm', 'msm.action', 'msm.util'],
    scripts=['bin/msm'],
    entry_points={'console_scripts': ['src=msn.command_line:main']}
)
