from setuptools import setup

setup(name='Py Word Cloud',
      version='1.0',
      description='A happy light weight word cloud generator in Python',
      url='https://github.com/iam-mhaseeb/py_word_cloud',
      author='Muhammad Haseeb',
      author_email='haseeb.emailbox@gmail.com',
      license='MIT',
      packages=['py_word_cloud'],
      install_requires=[
          'nltk', 'pillow'
      ],
      zip_safe=False)
