from setuptools import setup

setup(name='addtobuildlist',
      version='0.3.1',
      description='Print on output and on a unique log file ',
      url='https://github.com/Tibibv/addtobuildlist',
      author='Kron',
      author_email='kron_bv@yahoo.com',
      license='MIT',
      packages=['addtobuildlist'],
      install_requires=[
          'printandlog',
      ],
      zip_safe=False)
