#marcus's favorite number is 11, so example


#gio chose 852
count = 0
increment = 11
max_int = 2147483647
while count <= max_int:
    count += increment
if count > max_int:
    count -= increment

print(count)
