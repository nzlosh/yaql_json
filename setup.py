try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="yaql_json",
    version="0.1.14",
    author = "Carlos",
    author_email = "nzlosh@yahoo.com",
    packages=find_packages(),
    install_requires=["mistral", "yaql"],
    entry_points={
        "mistral.yaql_functions": [
            "to_json = yaql_json.json_converter:to_json",
            "from_json = yaql_json.json_converter:from_json"
        ]
    }
)
