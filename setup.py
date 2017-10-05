from distutils.core import setup
setup(
  name = 'gitfollow',
  packages = ['gitfollow'],
  version = '0.1',
  description = 'Github follower and following control',
  long_description="",
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/gitfollow',
  download_url = 'https://github.com/sepandhaghighi/gitfollow/tarball/v0.1',
  keywords = ['Follow', 'follower', 'github','python','git','stars','repo','stargazer'],
  install_requires=[
	  'codecov',
      'art',
      'requests',
      ],
  classifiers = [],
  license='MIT',
)
