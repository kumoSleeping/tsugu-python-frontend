from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='tsugu',
    version='2.0.4',
    author='kumoSleeping',
    author_email='zjr2992@outlook.com',
    license="MIT",
    description='Tsugu Python Frontend',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kumoSleeping/ChatTsuguPy',
    packages=find_packages(exclude=('test','test*')),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=[
            "loguru==0.7.2",
            "tsugu-api-python==1.2.0",
            "arclet-alconna==1.8.13",
        ],
    python_requires='>=3.8',
    include_package_data=False,

)