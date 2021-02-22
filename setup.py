from setuptools import find_packages, setup

setup(
    name='cryptic-sdk',
    packages=find_packages(),
    version='1.0.0',
    description='A Cryptic Client Library for Python',
    author='Tert0',
    license='MIT',
    install_requires=[
        'websocket-client',
    ],
    url='https://github.com/Tert0/cryptic-sdk',
)
