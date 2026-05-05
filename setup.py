from setuptools import setup

setup(
    name="vettel",
    version="1.1.0",
    author="cebem1nt",
    author_email='cebemnt@gmail.com',
    description="Get different formula 1 statistics and info",
    packages=["vettel"],
    py_modules=["vet"],
    include_package_data=True,
    package_data={"vettel": ["sql/*.sql"]},
    entry_points={
        "console_scripts": [
            "vet=vet:main"
        ]
    },
    install_requires=[],
    license="MIT",
)