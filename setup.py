from setuptools import setup

setup(
    name='nose-partitioner',
    version='0.1.0',
    description='Partition your tests and run partitions independently',
    author='Claudiu Coman',
    author_email='claud.coman@gmail.com',
    url='https://github.com/claudiu-coman/nose-partitioner',
    license='Apache 2.0',
    entry_points={
        'nose.plugins.0.10': [
            'partitioner = partitioner:Partitioner'
        ]
    },
    zip_safe=False,
    install_requires=['nose>=1.3.0'],
    keywords='nose nosetests partitioner nose-partitioner'
)
