import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name='env-man',  
     version='0.3.1',
     scripts=['env-man.py', 'env-man.config'],
     author="Rodrigo Del Bianco",
     author_email="rodrigo.fdb@gmail.com",
     description="Environment management utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/debianco/env_man",
     packages=setuptools.find_packages(),
     python_requires='>=2.7',
     include_package_data=True,
     package_data={
             '': ['env-man.config']
         },
     install_requires=[
             'PyInquirer',
             'pprint'
         ],
     classifiers=[
         "Programming Language :: Python :: 2",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )