from setuptools import find_packages, setup
setup(
    name='cryptic_client',
    packages=find_packages(),
    version='1.0.2',
    description='A Cryptic Client Library for Python',
    author='Tert0',
    license='MIT',
    install_requires=[
        'websocket-client',
    ],
    extra_requires=[
        'sphinx',
        'sphinx_rtd_theme'
    ],
    url='https://github.com/Tert0/cryptic-sdk',
)
