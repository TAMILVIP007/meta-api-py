import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mata_api",
    version="1.0.0",
    author="tamilvip007",
    author_email="indrajeethy.it20@scew.org",
    description="Python wrapper for MetaAvoid API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tamilvip007/mata_api",
    project_urls={
        "Bug Tracker": "https://github.com/tamilvip007/mata_api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "meta_api"},
    packages=setuptools.find_packages(where="meta_api"),
    python_requires=">=3.6",
)