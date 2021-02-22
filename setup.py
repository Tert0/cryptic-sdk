from setuptools import find_packages, setup

setup(
    name='cryptic_sdk',
    packages=find_packages(),
    version='1.0.1',
    description='A Cryptic Client Library for Python',
    author='Tert0',
    license='MIT',
    install_requires=[
        'websocket-client',
    ],
    url='https://github.com/Tert0/cryptic-sdk',
)
