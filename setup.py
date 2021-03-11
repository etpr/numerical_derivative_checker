from setuptools import setup, find_packages

setup(
    name='numerical_derivative_checker',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Simple numerical derivative checker with randomized input sampling.',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/etpr/numerical_derivative_checker',
    author='etpr',
    author_email='englertpr@gmail.com',
    include_package_data=True,
    python_requires=">=3.7"
)