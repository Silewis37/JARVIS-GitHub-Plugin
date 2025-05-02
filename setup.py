from setuptools import setup, find_packages

setup(
    name="jarvis_github_plugin",
    version="1.3.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3",
        "jarvis-api-library>=1.0.0",
    ],
    author="Samuel Lewis",
    description="A library for interacting with API's to be used within The J.A.R.V.I.S. Project.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)
