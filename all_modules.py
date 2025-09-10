import sys
import os

# Collect built-in module names
print("=== Built-in Modules ===")
for name in sys.builtin_module_names:
    print(name)

print("\n=== Installed Modules ===")

# Find site-packages path(s)
paths = sys.path

# Use a set to avoid duplicates
found_modules = set()

for path in paths:
    if not os.path.isdir(path):
        continue
    try:
        for entry in os.listdir(path):
            if entry.endswith(".py") and entry != "__init__.py":
                found_modules.add(entry[:-3])
            elif os.path.isdir(os.path.join(path, entry)):
                found_modules.add(entry)
    except PermissionError:
        continue

# Print found modules
for module in sorted(found_modules):
    print(module)
