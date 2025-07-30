
# list_top_level_modules.py
import sys, pkgutil

def main():
    names = {m.name for m in pkgutil.iter_modules()}          # installed modules/packages
    names |= set(sys.builtin_module_names)                    # add built-ins
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()

# list_all_importables_no_imports.py
import sys
import os
import pkgutil
from collections import deque

def package_dir(parent_dir, full_name):
    # full_name like "numpy.linalg" -> take last part "linalg" under parent_dir
    last = full_name.rsplit(".", 1)[-1]
    return os.path.join(parent_dir, last)

def main():
    seen = set(sys.builtin_module_names)  # include built-ins

    # Queue of (package_name, package_path) to process recursively
    to_visit = deque()

    # 1) Top-level modules/packages from each sys.path entry (no imports happen)
    for sp in sys.path:
        if not sp or not os.path.isdir(sp):
            continue
        for info in pkgutil.iter_modules([sp], prefix=""):
            seen.add(info.name)
            if info.ispkg:
                to_visit.append((info.name, package_dir(sp, info.name)))
