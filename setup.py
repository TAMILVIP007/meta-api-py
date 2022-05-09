import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name='meta_api',
    version='1.0.0',
    description='meta_api Wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    author='Tamilvip007',
    author_email='indrajeethy.it20@gmail.com',
    url='https://github.com/TAMILVIP007/meta_api.git',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Typing :: Typed'
    ],
    install_requires= ['requests'],
    python_requires='>=3.6'
)