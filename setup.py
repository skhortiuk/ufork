from pkg_resources import parse_requirements
from setuptools import setup

setup(
    name="ufork",
    version="18.2.1",
    author="Kurt Rose",
    author_email="kurt@kurtrose.com",
    description="A simple pre-forking container",
    license="BSD",
    url="http://github.com/doublereedkurt/ufork",
    packages=['ufork'],
    long_description='...',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
    ],
    install_requires=["six"]
)
