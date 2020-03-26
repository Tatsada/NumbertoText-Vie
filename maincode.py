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


def readSingleGroup(inputNum):
	readHundredDigit = (
	    listSingleDigit[int(inputNum[-3])] + " trăm") if len(inputNum) == 3 else ""
    # Đọc số hàng đơn vị
	if inputNum[-1] == "0":
	        readUnitDigit = ""
	elif inputNum[-1] == "1":
		if inputNum[-2] == "0" or inputNum[-2] == "1" or len(inputNum)==1:
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
    '''if len(inputNum) == 3:		# Đủ 3 chữ số
        readHundredDigit = listSingleDigit[int(inputNum[-3])] + " trăm"
        # Đọc số hàng chục
        if inputNum[-2] == "1":
            readTenDigit = " mười"
        elif inputNum[-2] == "0":
            if inputNum[-1] == "0":
                readTenDigit = ""
            else:
                readTenDigit = " linh"
        else:
            readTenDigit = " " + listSingleDigit[int(inputNum[-2])] + " mươi"
        # Đọc số hàng đơn vị
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
    elif len(inputNum) == 2:
        readHundredDigit = ""
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
    else:
        readHundredDigit = ""
        readTenDigit = ""
        readUnitDigit = listSingleDigit[int(inputNum)]
    return readHundredDigit + readTenDigit + readUnitDigit'''


def numberToText(inputNum):
    listGroupToText = []
    for i in range(len(splitDigitGroup(inputNum)) - 1, -1, -1):
        listGroupToText.append(readSingleGroup(splitDigitGroup(inputNum)[i]))
        listGroupToText.append(listDigitGroup[i])
    return " ".join(listGroupToText)


n = input("Nhập số : ")
print("Số đọc là:", numberToText(n))
