n=90
for i in range(1,n):
    if i < 32:
        print(f"2024-01-{i}")
    elif i < 61:
        print(f"2024-02-{i-31}")
    else:
        print(f"2024-03-{i-60}")