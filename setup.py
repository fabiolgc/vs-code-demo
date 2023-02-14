import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbdf_hello-world",
    version="0.0.1",
    author="Julian Shalaby",
    author_email="julian.shalaby@databricks.com",
    description="Databricks Detection Framework Hello World",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/databricks/dbdf-hello-world",
    package_dir={'': 'src'},
    packages=setuptools.find_packages("src", exclude=["tests"]),
    install_requires=[
        "pyspark"
    ],
    tests_require=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.5',
)
