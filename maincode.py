def splitDigitGroup(inputNum):
    numOfDigit = len(inputNum)
    numOfDigitGroup = numOfDigit // 3 + 1
    digitGroup = [inputNum[-3:]]
    for i in range(1, numOfDigitGroup - 1):
        digitGroup.append(inputNum[-(3 * i + 3):-3 * i])
    return digitGroup


def readSingleGroup(inputNum):
    listSingleDigit = ["không", "một", "hai", "ba",
                       "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if int(inputNum) < 99:
        return readTenAndUnitDigit(inputNum)
    else:
        if inputNum[-2] == "0":
            if inputNum[-1] == "0":
                readTwoLastDigit = ""
            else:
                readTwoLastDigit = "linh " + listSingleDigit[int(inputNum[-1])]
        else:
            readTwoLastDigit = readTenAndUnitDigit(inputNum)
        return listSingleDigit[int(inputNum[-3])] + " trăm " + readTwoLastDigit


def readTenAndUnitDigit(inputNum):
    listSingleDigit = ["không", "một", "hai", "ba",
                       "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if int(inputNum) <= 9:
        return listSingleDigit[int(inputNum)]
    else:
        if inputNum[-2] == "1":
            readTenDigit = "mười"
        else:
            readTenDigit = listSingleDigit[int(inputNum[-2])] + " mươi"
        if inputNum[-1] == "0":
            readUnitDigit = ""
        elif inputNum[-1] == "5":
            readUnitDigit = "lăm"
        else:
            readUnitDigit = listSingleDigit[int(inputNum[-1])]
    return readTenDigit + " " + readUnitDigit


def numberToText(inputNum):
    listDigitGroup = ["", "nghìn", "triệu", "tỷ"]
    numberToTex = ""
    for i in range(len(splitDigitGroup(inputNum)) - 1, -1, -1):
        numberToTex += (" " + readSingleGroup(splitDigitGroup(inputNum)
                                              [i]) + " " + listDigitGroup[i])
    return numberToTex


n = input("Nhập số : ")
print("Số đọc là:", numberToText(n))
