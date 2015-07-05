from distutils.core import setup
setup(
  name = 'buildbot-try',
  packages = ['buildbot_try'],
  version = '0.1.2',
  description = 'Buildbot Try Client',
  author = 'Varun Sharma',
  author_email = 'varun@sharmalabs.org',
  url = 'https://github.com/varunsharma/buildbot-try',
#  download_url = 'https://github.com/varunsharma/buildbot-try/tarball/0.1',
  keywords = ['buildbot', 'try client', 'continous inegration'],
  classifiers = [],
  entry_points = { 
    'console_scripts': ['buildtry = buildbot_try.base:tryclient',]
                    },  
    install_requires = ['requests',],
)
