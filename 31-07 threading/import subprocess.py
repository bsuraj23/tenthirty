import subprocess

result=subprocess.run(["echo","hello here!"], capture_output=True, text=True, shell=True)

print("output",result.stdout)
print("Exit code", result.returncode)