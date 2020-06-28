def shape(arr, isHour=False, isMin=False):
    if isHour:
        a = [i for i in arr if i < 12]
    if isMin:
        a = [i for i in arr if i < 60]
    return a

def main():
    arr = []
    arr.append(1)
    arr.append(2)
    arr.append(4)
    arr.append(8)
    arr.append(16)
    arr.append(32)

    a = []
    a = shape(arr, True, True)

    print(a)

if __name__ == "__main__":
    main()
