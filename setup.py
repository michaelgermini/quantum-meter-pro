#!/usr/bin/env python3
"""
Setup script for QuantumMeter Pro
Advanced Laboratory Software for Quantum Measurement Devices
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="quantum-meter-pro",
    version="1.0.0",
    author="QuantumMeter Pro Team",
    author_email="support@quantum-meter-pro.com",
    description="Advanced Laboratory Software for Quantum Measurement Devices",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quantum-meter-pro",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Measurement",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "quantum-meter-pro=main:main",
            "quantum-meter-web=src.web.app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.csv", "*.html", "*.css", "*.js"],
    },
    keywords="quantum, measurement, laboratory, physics, science, research",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/quantum-meter-pro/issues",
        "Source": "https://github.com/yourusername/quantum-meter-pro",
        "Documentation": "https://github.com/yourusername/quantum-meter-pro/wiki",
    },
)
