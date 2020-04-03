import math
listSingleDigit = ["không", "một", "hai", "ba",
                   "bốn", "năm", "sáu", "bảy", "tám", "chín"]
listDigitGroup = ["", "nghìn", "triệu", "tỷ"]


def splitDigitGroup(inputNum):
    numOfDigitGroup = math.ceil(len(inputNum) / 3)
    if numOfDigitGroup == 1:
        digitGroup = [(inputNum)]
    else:
        tempInputNum = inputNum
        i = 1
        digitGroup = []
        while i <= numOfDigitGroup:
            digitGroup.append(tempInputNum[-3:])
            tempInputNum = tempInputNum[:-3]
            i += 1
    return digitGroup


def readSingleGroup(inputNum):

    # Đọc số hàng trăm
    readHundredDigit = (
        listSingleDigit[int(inputNum[-3])] + " trăm") if len(inputNum) == 3 else ""

    # Đọc số hàng đơn vị
    if len(inputNum) >= 2:
        if inputNum[-1] == "0":
            readUnitDigit = ""
        elif inputNum[-1] == "1":
            readUnitDigit = " một" if inputNum[-2] == "0" or inputNum[-2] == "1" else " mốt"
        elif inputNum[-1] == "5":
            readUnitDigit = " năm" if inputNum[-2] == "0" else " lăm"
        else:
            readUnitDigit = " " + listSingleDigit[int(inputNum[-1])]
    else:
        readUnitDigit = " " + listSingleDigit[int(inputNum[-1])]

    # Đọc số hàng chục
    if len(inputNum) >= 2:
        if inputNum[-2] == "1":
            readTenDigit = " mười"
        elif inputNum[-2] == "0":
            readTenDigit = "" if inputNum[-1] == "0" else " linh"
        else:
            readTenDigit = " " + listSingleDigit[int(inputNum[-2])] + " mươi"
    else:
        readTenDigit = ""
    return readHundredDigit + readTenDigit + readUnitDigit


def numberToText(inputNum):
    listGroupToText = []
    for i in range(len(splitDigitGroup(inputNum)) - 1, -1, -1):
        listGroupToText.append(readSingleGroup(splitDigitGroup(inputNum)[i]))
        listGroupToText.append(listDigitGroup[i])
    return " ".join(listGroupToText)


n = input("Nhập số : ")
print("Số đọc là:", numberToText(n))
