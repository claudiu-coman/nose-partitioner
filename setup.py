from setuptools import setup, find_packages

setup(
    name='nose-partitioner',
    version='0.1.0',
    description='Partition your tests and run partitions independently',
    author='Claudiu Coman',
    author_email='claud.coman@gmail.com',
    url='https://github.com/claudiu-coman/nose-partitioner',
    license='Apache 2.0',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['nose>=1.3.0'],
    keywords='nose partitioner nose-partitioner'
)
