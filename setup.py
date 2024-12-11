# ----------------------------------------------------------------------------
# Copyright (c) 2016-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages
import versioneer

setup(
    name='moshpit',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD-3-Clause',
    url='https://bokulich-lab.github.io/moshpit-docs/intro.html',
    packages=find_packages(),
    include_package_data=True,
    scripts=['bin/tab-mosh'],
    entry_points={
        'console_scripts': [
            'mosh=moshpit.__main__:mosh'
        ]
    },
    zip_safe=False,
)
