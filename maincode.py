import math
listSingleDigit = ["không", "một", "hai", "ba",
                   "bốn", "năm", "sáu", "bảy", "tám", "chín"]
listDigitGroup = ["", "nghìn", "triệu", "tỷ"]


def splitDigitGroup(inputNum):
    numOfDigitGroup = math.ceil(len(inputNum) / 3)
    if numOfDigitGroup == 1:
        digitGroup = list(inputNum)
    else:
        tempInputNum = inputNum
        i = 1
        digitGroup = []
        while i <= numOfDigitGroup:
            digitGroup.append(tempInputNum[-3:])
            tempInputNum = tempInputNum[:-3]
            i += 1
    return digitGroup


def readSingleGroupFull(inputNum):
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


def readSingleGroupMissing(inputNum):
    if len(inputNum) == 1:
        return listSingleDigit[int(inputNum)]
    else:
        if inputNum[-2] == "1":
            readTenDigit = "mười"
        else:
            readTenDigit = listSingleDigit[int(inputNum[-2])] + " mươi"

        if inputNum[-1] == "0":
            readUnitDigit = ""
        elif inputNum[-1] == "1":
            if inputNum[-2] == "1":
                readUnitDigit = " một"
            else:
                readUnitDigit = " mốt"
        elif inputNum[-1] == "5":
            readUnitDigit = " lăm"
        else:
            readUnitDigit = " " + listSingleDigit[int(inputNum[-1])]

        return readTenDigit + readUnitDigit


def numberToText(inputNum):
    listGroupToText = []
    for i in range(len(splitDigitGroup(inputNum)) - 1, -1, -1):
        if len(splitDigitGroup(inputNum)[i]) < 3:
            listGroupToText.append(readSingleGroupMissing(
                splitDigitGroup(inputNum)[i]))
            listGroupToText.append(listDigitGroup[i])
        else:
            listGroupToText.append(readSingleGroupFull(
                splitDigitGroup(inputNum)[i]))
            listGroupToText.append(listDigitGroup[i])
    return " ".join(listGroupToText)


n = input("Nhập số : ")
print("Số đọc là:", numberToText(n))
