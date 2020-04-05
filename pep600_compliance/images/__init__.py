from pep600_compliance.images.os.alt import ALT_LIST
from pep600_compliance.images.os.amazonlinux import AMAZONLINUX_LIST
from pep600_compliance.images.os.archlinux import ARCHLINUX_LIST
from pep600_compliance.images.os.centos import CENTOS_LIST
from pep600_compliance.images.os.clearlinux import CLEARLINUX_LIST
from pep600_compliance.images.os.debian import DEBIAN_LIST
from pep600_compliance.images.os.fedora import FEDORA_LIST
from pep600_compliance.images.os.mageia import MAGEIA_LIST
from pep600_compliance.images.os.opensuse import OPENSUSE_LIST
from pep600_compliance.images.os.oraclelinux import ORACLELINUX_LIST
from pep600_compliance.images.os.photon import PHOTON_LIST
from pep600_compliance.images.os.ubuntu import UBUNTU_LIST


IMAGE_LIST = ALT_LIST + AMAZONLINUX_LIST + ARCHLINUX_LIST + CENTOS_LIST + CLEARLINUX_LIST + DEBIAN_LIST + FEDORA_LIST + MAGEIA_LIST + OPENSUSE_LIST + ORACLELINUX_LIST + PHOTON_LIST + UBUNTU_LIST


def get_images(machine):
    for image in IMAGE_LIST:
        if machine in image.machines:
            yield image
