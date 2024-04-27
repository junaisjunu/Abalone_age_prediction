from setuptools import find_packages, setup

setup(
    name='Abalone Age prediction',
    version='0.0.1',
    author='Junais',
    author_email='junaisk456@gmail.com',
    install_requires=["scikit-learn", "pandas", "numpy"],
    packages=find_packages()
)
