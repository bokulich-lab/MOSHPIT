# ----------------------------------------------------------------------------
# Copyright (c) 2024, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import sys
import qiime2
import importlib

try:
    from ._version import __version__
except ModuleNotFoundError:
    __version__ = '0.0.0+notfound'


def __getattr__(name):
    self = sys.modules[__name__].__dict__
    try:
        # mostly for __version__, but could handle other things
        return getattr(self, name)
    except AttributeError:
        try:
            return getattr(qiime2, name)
        except AttributeError:
            # this is just to raise the right error
            getattr(self, name)


def __dir__():
    return dir(qiime2)


class __QIIMEProxyImport:
    def find_spec(self, name, path=None, target=None):
        if not name.startswith('moshpit'):
            return None
        if target is not None:
            # TODO: experiment with this to see if it is possible
            raise ImportError("Reloading the moshpit API is not"
                              " currently supported.")
        fqn = name.split('.')
        fqn[0] = 'qiime2'
        resolved = '.'.join(fqn)

        try:
            # jimmy it onto our module for the forward import search
            module = importlib.import_module(resolved)
            sys.modules[name] = module
        except ModuleNotFoundError:
            return None

        return importlib.util.find_spec(resolved)


sys.meta_path += [__QIIMEProxyImport()]
