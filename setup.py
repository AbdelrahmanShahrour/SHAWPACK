from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()
description = 'Now with us, dealing with Arabic texts has become easy, and in the future it will become easier with us'
ver = '0.0.2'


setup(
    name='SHAWPACK',
    version= ver,
    install_requires=required,
    tests_require=['pytest'],
    author="AbdelrahmanShahrour",
    long_description=description,
    long_description_content_type='text/x-rst',
    url='https://github.com/AbdelrahmanShahrour/SHAWPACK',
    keywords=['NLP', 'text-data', 'AI', 'DS', 'Shahrour', 'arabic-py', 'arabic-nlp'],
    description="SHAWPACK NLP processing package",
    packages=find_packages(include=['shawpack'])
)
