from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mkdataset',
    version='0.1',
    author="Hemanth Reddy",
    author_email="hemanth346@gmail.com",
    description="Utility to create image datasets from feed of webcam or Video file",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/hemanth346/mkdataset",
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Environment :: Console',
		'Intended Audience :: Other Audience', # Computer Vision Engineers, Deep Learning Engineers, Data Scientists
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		'Topic :: Software Development :: Build Tools'
    ],

    install_requires=[
        'Click',
        'opencv-python',
        'numpy',
    ],
    entry_points='''
        [console_scripts]
        saveimg=saveimg.cli:save
    ''',
)