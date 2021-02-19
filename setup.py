import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="json_tagger",
    version="1.0.0",
    author="Richard Smith",
    author_email="richard.d.smith@stfc.ac.uk",
    description="description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cedadev/json_tagger.git",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'directory_tree'
    ]
)
