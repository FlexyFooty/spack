# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyZopeInterface(PythonPackage):
    """This package provides an implementation of "object interfaces" for
    Python. Interfaces are a mechanism for labeling objects as conforming to a
    given API or contract. So, this package can be considered as implementation
    of the Design By Contract methodology support in Python."""

    homepage = "https://github.com/zopefoundation/zope.interface"
    pypi = "zope.interface/zope.interface-4.5.0.tar.gz"

    license("ZPL-2.1")

    version("5.4.0", sha256="5dba5f530fec3f0988d83b78cc591b58c0b6eb8431a85edd1569a0539a8a5a0e")
    version("5.1.0", sha256="40e4c42bd27ed3c11b2c983fecfb03356fae1209de10686d03c02c8696a1d90e")
    version("4.5.0", sha256="57c38470d9f57e37afb460c399eb254e7193ac7fb8042bd09bdc001981a9c74c")

    depends_on("c", type="build")  # generated

    depends_on("python@2.7:2.8,3.4:", type=("build", "run"), when="@4.5.0")
    depends_on("python@2.7:2.8,3.5:", type=("build", "run"), when="@5.1.0:")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-setuptools@:45", type=("build", "run"), when="@4.5.0")
