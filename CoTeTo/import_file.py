#!/usr/bin/env python3

import sys
import importlib


def import_file(module_path='', module=''):
    importlib.invalidate_caches()
    if module in sys.modules:
        del sys.modules[module]
    sys.path.insert(0, module_path)
    spec = importlib.util.find_spec(module)
    m = spec.loader.load_module()
    del sys.path[0]
    return m


if __name__ == '__main__':
    # test this module with path and module name as arguments
    # will print modules namespace (without __builtins__)

    import pprint

    p, n = sys.argv[1:]
    m = import_file(p, n)
    d = m.__dict__
    del d['__builtins__']
    pprint.pprint(d)
