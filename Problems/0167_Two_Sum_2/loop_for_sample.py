def main():
    numbers = [0]*10
    
    for i in range(len(numbers)):
        numbers[i] = i

    for i in range(len(numbers)):
        print("numbers[%d] = %s" %(i, numbers[i]))


if __name__ == "__main__":
    main()
