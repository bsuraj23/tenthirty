
# list_top_level_modules.py
import sys, pkgutil

def main():
    names = {m.name for m in pkgutil.iter_modules()}          # installed modules/packages
    names |= set(sys.builtin_module_names)                    # add built-ins
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()

