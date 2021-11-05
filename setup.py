from setuptools import setup


setup(name='speed_calculator',
version='0.1.1',
description="""A library to speed calculation of a function.""",
long_description="""
# Speed Calculator
A library to speed calculation of a function.
# Install
```
pip3 install speed-calculator
```
# Using
```python
from speed_calculator import calculate

import time
def a_function():
    time.sleep(2)

print(calculate(a_function))
```
""",
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/speed_calculator',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["speed_calculator"],
package_dir={'':'src'},
python_requires=">= 3",
zip_safe=False)