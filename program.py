print("My first program")
print("Hello World")
print("Say Goodbye")
print("bye bye")
for i in range(1,100):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
        else:
            pass
    if count == 2:
        print(i)
    else:
        pass