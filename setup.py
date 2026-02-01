from setuptools import setup, find_packages

setup(
    name="myshark",
    version="1.0.0",
    author="naveen-anon",
    author_email="",
    description="Offline Wireshark-style CLI tool for PCAP analysis",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/naveen-anon/myshark",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "myshark=myshark.myshark:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Environment :: Console",
    ],
)
