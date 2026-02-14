from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

setup(
    name="Topsis-Naman-102317144",
    version="1.0.3",
    author="Naman Singh",
    author_email="nsingh1_be23@thapar.edu",
    description="A Python package to perform TOPSIS analysis for multi-criteria decision making",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/naman-singh/topsis-package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    entry_points={
        'console_scripts': [
            'topsis=Topsis_Naman_102317144.__main__:main',
        ],
    },
)
