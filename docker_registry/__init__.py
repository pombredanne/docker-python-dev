# -*- coding: utf-8 -*-
# DON'T alter the following, or add anything else in here
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)
