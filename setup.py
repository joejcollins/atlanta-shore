import setuptools

setuptools.setup(
    name="atlanta-shore",
    version="1.0",
    author="Joe J Collins",
    author_email="joejcollins@gmail.com",
    description="",
    license="MIT License",
    url="https://github.com/joejcollins/atlanta-shore",
    packages=setuptools.find_packages(),
    package_dir={"": "./"},
    classifiers=["Development Status :: 3 - Alpha", "License :: Other/Proprietary License"],
    install_requires=[
        "black",
        "debugpy",  # only required for debugging, not needed for production.
        "flake8",
        "lxml",  # for parsing GPX files.
        "mypy",
        "pip-tools",  # used to manage requirements.txt.
        "pytest",  # used for testing, not needed for production.
    ],
)