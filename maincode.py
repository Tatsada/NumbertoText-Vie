listSingleDigit = ["không", "một", "hai", "ba",
                   "bốn", "năm", "sáu", "bảy", "tám", "chín"]
listDigitGroup = ["", "nghìn", "triệu", "tỷ"]


def splitDigitGroup(inputNum):
    numOfDigitGroup = (len(inputNum) // 3) + 1
    digitGroup = [inputNum[-3:]]
    for i in range(1, numOfDigitGroup - 1):
        digitGroup.append(inputNum[-(3 * i + 3):-3 * i])
    return digitGroup


def readSingleGroup(inputNum):
    readHundredDigit = listSingleDigit[int(inputNum[-3])] + " trăm"

    if inputNum[-2] == "1":
        readTenDigit = " mười"
    elif inputNum[-2] == "0":
        if inputNum[-1] == "0":
            readTenDigit = ""
        else:
            readTenDigit = " linh"
    else:
        readTenDigit = " " + listSingleDigit[int(inputNum[-2])] + " mươi"

    if inputNum[-1] == "0":
        readUnitDigit = ""
    elif inputNum[-1] == "1":
        if inputNum[-2] == "0" or inputNum[-2] == "1":
            readUnitDigit = " một"
        else:
            readUnitDigit = " mốt"
    elif inputNum[-1] == "5":
        if inputNum[-2] == "0":
            readUnitDigit = " năm"
        else:
            readUnitDigit = " lăm"
    else:
        readUnitDigit = " " + listSingleDigit[int(inputNum[-1])]

    return readHundredDigit + readTenDigit + readUnitDigit


def numberToText(inputNum):
    numberToText = ""
    for i in range(len(splitDigitGroup(inputNum)) - 1, -1, -1):
        numberToText += (readSingleGroup(splitDigitGroup(inputNum)
                                               [i]) + " " + listDigitGroup[i])
    return numberToText


n = input("Nhập số : ")
print("Số đọc là:", numberToText(n))
