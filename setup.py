from setuptools import setup, find_packages

setup(
    name="brahmastra",
    version="0.1.0",
    author="Nikhil Nishad",
    author_email="nikhil.nishad@outlook.in",
    description="The Brahmastra is an undetected WebDriver, "
                "inspired by the legendary weapon of unparalleled power and destruction."
                " Just like its mythical namesake, this tool is designed to be a formidable "
                "asset in your automation arsenal. It allows you to navigate any website or"
                " webpage effortlessly and invisibly, bypassing anti-bot measures with ease. "
                "With Brahmastra, automating your web tasks becomes seamless and worry-free, "
                "making it an indispensable tool for developers and automation enthusiasts alike.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nnishad/brahmastra",
    packages=find_packages(),
    install_requires=[
        "undetected-chromedriver",
        "fake-useragent",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)