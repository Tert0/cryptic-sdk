from setuptools import find_packages, setup

readme = open('README.md', 'r').read()

setup(
    name='cryptic_sdk',
    packages=find_packages(),
    version='1.0.7',
    description='A Cryptic SDK for Python',
    long_description=readme,
    long_description_content_type="text/markdown",
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
    python_requires=">=3.5"
)
