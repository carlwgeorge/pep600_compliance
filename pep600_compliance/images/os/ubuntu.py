from pep600_compliance.images import base
from pep600_compliance.images import package_manager


class Ubuntu(base.Base):
    def __init__(self, image, eol, machines, packages, apt_sources_update=[], ppa_list=[], python='python3'):
        name, version = image.split(':')
        self._packages = packages
        super().__init__(image, name, version, eol, package_manager.APT(run_once=apt_sources_update, ppa_list=ppa_list), machines=machines, python=python)

    def install_packages(self, container, machine):
        super()._install_packages(container, machine, self._packages)


UBUNTU_APT_OLD = [
    ['sed', '-i', 's,archive.ubuntu.com,old-releases.ubuntu.com,g', '/etc/apt/sources.list'],
    ['sed', '-i', 's,security.ubuntu.com,old-releases.ubuntu.com,g', '/etc/apt/sources.list'],
    ['sed', '-i', 's,ports.ubuntu.com/ubuntu-ports,old-releases.ubuntu.com/ubuntu,g', '/etc/apt/sources.list'],
]
UBUNTU_PYTHON_PPA = [
    'ppa:fkrull/deadsnakes'
]

UBUNTU_PACKAGES = ['libx11-6', 'libxext6', 'libxrender1', 'libice6', 'libsm6', 'libgl1-mesa-glx', 'libglib2.0-0']
UBUNTU_LIST = [
    # EOL info: https://wiki.ubuntu.com/Releases
    Ubuntu('ubuntu:20.10', '2021-07-17', machines=['x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES]),
    Ubuntu('ubuntu:20.04', None, machines=['x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES]),
    Ubuntu('ubuntu:19.10', '2020-07-17', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES]),
    Ubuntu('ubuntu:19.04', '2020-01-23', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES]),
    Ubuntu('ubuntu:18.10', '2019-07-18', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:18.04', '2028-04-30', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES]),
    Ubuntu('ubuntu:17.10', '2018-07-19', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:17.04', '2018-01-13', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:16.10', '2017-07-20', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:16.04', '2024-04-30', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 's390x', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES]),
    Ubuntu('ubuntu:15.10', '2016-07-28', machines=['i686', 'x86_64'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:15.04', '2016-02-04', machines=['i686', 'x86_64'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:14.10', '2015-07-23', machines=['x86_64'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:14.04', '2022-04-30', machines=['i686', 'x86_64', 'aarch64', 'ppc64le', 'armv7l'], packages=[['python3-pip'] + UBUNTU_PACKAGES]),
    Ubuntu('ubuntu:13.10', '2014-07-17', machines=['x86_64'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:13.04', '2014-01-27', machines=['x86_64'], packages=[['python3-pip'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD),
    Ubuntu('ubuntu:12.10', '2014-05-16', machines=['x86_64'], packages=[['python3.4'] + UBUNTU_PACKAGES], apt_sources_update=UBUNTU_APT_OLD, python='python3.4', ppa_list=UBUNTU_PYTHON_PPA),
    Ubuntu('ubuntu:12.04', '2019-04-30', machines=['x86_64'], packages=[['python3.5', 'curl'] + UBUNTU_PACKAGES], python='python3.5', ppa_list=UBUNTU_PYTHON_PPA),
]
