from pathlib import Path

from setuptools import setup


def read_version() -> str:
    for line in Path("app.py").read_text().splitlines():
        if line.startswith("__version__"):
            return line.split("=")[1].strip().strip('"').strip("'")
    raise RuntimeError("Unable to determine version from app.py")


setup(
    name="fedmed-pl-supernode",
    version=read_version(),
    description="Flower client ChRIS plugin used in the FedMed demo",
    author="FedMed BU Team",
    author_email="rpsmith@bu.edu",
    url="https://github.com/FNNDSC/pl-supernode",
    py_modules=["app"],
    install_requires=[
        "chris_plugin==0.4.0",
        "flwr>=1.23.0,<2",
        "torch>=2.1.0",
        "torchvision>=0.16.0",
        "medmnist>=3.0.1",
    ],
    license="MIT",
    entry_points={
        "console_scripts": [
            "fedmed-pl-supernode = app:main",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    extras_require={"none": [], "dev": []},
)
