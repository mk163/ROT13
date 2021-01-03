import random

def rotN(N,cha):
    list = []
    for i in range(len(cha)):
        c = cha[i]
        num = ord(cha[i])
        if num > 0x7a - N:
            num = num - 26 + N
        else:
            num += N
        list.append(chr(num))
    result = "".join(list)
    print(result)
    return result

def main():
    print('今回はROT' + str(N) + 'です')

    print("文字列を入力してください")
    cha = input()

    rotN(N,cha)

if __name__ == "__main__":
    main()
