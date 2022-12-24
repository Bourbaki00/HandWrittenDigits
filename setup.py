
import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='HandWriitenDigits',
      version='0.0.1',
      description='Hand Written Digit Classification',
      author='Shauray Singh',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['numpy', 'requests', 'pillow', 'networkx'],
      python_requires='>=3.8',
      extras_require={
        'testing': [
            "pytest",
            "torch~=1.11.0",
            "tqdm",
            "protobuf~=3.19.0",
            "onnx",
            "onnx2torch",
            "mypy",
        ],
      },
      include_package_data=True)
