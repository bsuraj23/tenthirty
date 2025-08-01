
# list_top_level_modules.py
import sys, pkgutil

def main():
    names = {m.name for m in pkgutil.iter_modules()}          # installed modules/packages
    names |= set(sys.builtin_module_names)                    # add built-ins
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()

#List all importable names (including subpackages/submodules)
#list_all_importables.py
import sys, pkgutil

def main():
    seen = set(sys.builtin_module_names)
    for info in pkgutil.walk_packages():     # walks recursively
        seen.add(info.name)                  # fully qualified name, e.g., numpy.linalg
    for name in sorted(seen):
        print(name)

if __name__ == "__main__":
    main()