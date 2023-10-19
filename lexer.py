#TJ Bourget was here

class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def tokenize(srcCode):
    tokSeq = []
    while srcCode != "":
        char = srcCode[0]

        if char == "+":
            newToken = token("PLUS",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == "-":
            newToken = token("MINUS",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == "*":
            newToken = token("MULTIPLICATION",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == "/":
            newToken = token("DIVISION",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == "(":
            newToken = token("LPAREN",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == ")":
            newToken = token("RPAREN",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == " ":
            srcCode = srcCode[1:]
            pass

        elif char.isdigit():
            numbStr = ""
            while char.isdigit():
                numbStr += char
                srcCode = srcCode[1:]
                if srcCode == "":
                    char = srcCode
                else:
                    char = srcCode[0]
            newToken = token("NUMBER",numbStr)
            tokSeq.append(newToken)

    return tokSeq

