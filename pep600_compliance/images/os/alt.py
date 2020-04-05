from pep600_compliance.images import base
from pep600_compliance.images import package_manager


class Alt(base.Base):
    def __init__(self, image, packages, machines):
        name, version = image.split(':')
        self._packages = packages
        super().__init__(image, name, version, package_manager.APT(has_no_install_recommends=False), machines=machines)

    def install_packages(self, container, machine):
        super()._install_packages(container, machine, self._packages)


ALT_PACKAGES = ['python3-module-pip', 'libX11', 'libXext', 'libXrender', 'libICE', 'libSM', 'libGL', 'glib2']
ALT_LIST = [
    Alt('alt:sisyphus', machines=['i686', 'x86_64', 'aarch64', 'ppc64le'], packages=[['libnsl1'] + ALT_PACKAGES]),
    Alt('alt:p9', machines=['i686', 'x86_64', 'aarch64', 'ppc64le'], packages=[['libnsl1'] + ALT_PACKAGES]),
    Alt('alt:p8', machines=['i686', 'x86_64'], packages=[ALT_PACKAGES]),
]
