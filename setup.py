from setuptools import setup

setup(name='miniflow',
      version='0.1.1',
      description='something',
      url='https://github.com/sbartek/miniflow',
      author='Flying Circus',
      author_email='bartekskorulski@gmail.com',
      license='MIT',
      packages=['miniflow'],
      install_requires=[
          'numpy',
          'pyhamcrest'
      ],
      zip_safe=False)
