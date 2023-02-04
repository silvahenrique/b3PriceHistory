from setuptools import find_packages, setup
setup(
    name='b3PriceHistory',
    packages=find_packages(include=['b3PriceHistory']),
    version='0.1.0',
    description='My first Python library',
    author='Silva, Henrique',
    license='',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
