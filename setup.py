from setuptools import setup

setup(
    name="vettel",
    version="1.0.0",
    author="cebem1nt",
    author_email='cebemnt@gmail.com',
    description="A cli tool to gather different statistics and info from f1db ",
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