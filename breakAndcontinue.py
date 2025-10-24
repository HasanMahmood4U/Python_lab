for i in range(1, 10):
    
    if i == 3:
        continue    # Skips printing 3

    if i == 5:
        pass        # Does nothing, execution continues
    
    if i == 8:
        break       # Loop stops when i becomes 8

    print(i)
