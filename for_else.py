successful = False

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Tried 3 times and failed")
