import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()
setuptools.setup(
   name='pyliwcbr',
   version='0.0.1',
   author="Wesley Ferreira",
   author_email="ovvesley@protonmail.com",
   description="Biblioteca de acesso ao dicionário Liwc",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="www.github.com/ovvesley/pyliwcbr",
   packages= setuptools.find_packages(),
   install_requires=["required_packages"],
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
)

#pip install git+https://github.com/jkbr/httpie.git#egg=httpie
