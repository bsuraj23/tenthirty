import time

print("start")
time.sleep(2)
print("end")

print(time.time())


start = time.time()
# some code
end = time.time()
print("Execution time:", end - start, "seconds")
