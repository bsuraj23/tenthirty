data1 = "hello world"
data2 = ['a', 'b', 'c', 'a', 'd', 'a', 'b']

char1, count1 = most_repeated_char(data1)
char2, count2 = most_repeated_char(data2)

print(f"Most repeated in '{data1}': '{char1}' (appears {count1} times)")
print(f"Most repeated in {data2}: '{char2}' (appears {count2} times)")
