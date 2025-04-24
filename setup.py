import setuptools

with open("README.md", "r", encoding= "utf-8" ) as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-end-Wine-Quality-Prediction-Project"
AUTHOR_USER_NAME = 'yashshivankar'
SRC_REPO = 'WineQualityPrediction'
AUTHOR_EMAIL = "yshivankar601@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "BUG Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)

# now in requirements.txt file at the end i write " -e ." 
# this command automatically look for setup.py file and install it