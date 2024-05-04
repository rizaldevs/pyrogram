from setuptools import setup, find_packages

# Membaca isi dari requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="Pyrozal",
    version="1.0",
    packages=find_packages(),
    description='Fork Pyrogram',
    author="rizaldevs",
    author_email="rizaldaitona@gmail.com",
    url="https://t.me/pyrogram",
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
)

