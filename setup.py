import  io
from setuptools import setup

with io.open('README.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(name='pywordcloudy',
      version='1.1',
      description='A happy light weight word cloud generator in Python',
      long_description=readme,
      long_description_content_type='text/markdown',
      keywords='wordcloud textprocessing',
      url='https://github.com/iam-mhaseeb/pywordcloudy',
      author='Muhammad Haseeb',
      author_email='haseeb.emailbox@gmail.com',
      license='MIT',
      packages=['pywordcloudy'],
      install_requires=[
          'nltk', 'pillow'
      ],
      data_files=[('static', [
          'pywordcloudy/font.ttf', 'pywordcloudy/stop_words_list.txt'])],
      zip_safe=False,
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      )

