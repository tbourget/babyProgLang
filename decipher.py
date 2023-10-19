#TJ Bourget was here

def decipher(babyExp):

    srcCode = ""
    babyExpArray = list(babyExp)
    babyExpArray.append(" ")
    babyWord = ""
    for index in range(len(babyExpArray)):
        if(babyExpArray[index] != " "):
            babyWord += babyExpArray[index]

            if(babyWord == "pee"):
                srcCode += "+"
                babyWord = ""
            elif(babyWord == "gah"):
                srcCode += "-"
                babyWord = ""
            elif (babyWord == "milk"):
                srcCode += "*"
                babyWord = ""
            elif (babyWord == "heh"):
                srcCode += "/"
                babyWord = ""
            elif (babyWord == "mama"):
                srcCode += "("
                babyWord = ""
            elif (babyWord == "dada"):
                srcCode += ")"
                babyWord = ""
            elif(babyWord == "b" and babyExpArray[index+1] != 'a'):
                srcCode += "0"
                babyWord = ""
            elif(babyWord == "ba" and babyExpArray[index+1] != 'a'):
                srcCode += "1"
                babyWord = ""
            elif (babyWord == "baa" and babyExpArray[index + 1] != 'a'):
                srcCode += "2"
                babyWord = ""
            elif (babyWord == "baaa" and babyExpArray[index + 1] != 'a'):
                srcCode += "3"
                babyWord = ""
            elif (babyWord == "baaaa" and babyExpArray[index + 1] != 'a'):
                srcCode += "4"
                babyWord = ""
            elif (babyWord == "baaaaa" and babyExpArray[index + 1] != 'a'):
                srcCode += "5"
                babyWord = ""
            elif (babyWord == "baaaaaa" and babyExpArray[index + 1] != 'a'):
                srcCode += "6"
                babyWord = ""
            elif (babyWord == "baaaaaaa" and babyExpArray[index + 1] != 'a'):
                srcCode += "7"
                babyWord = ""
            elif (babyWord == "baaaaaaaa" and babyExpArray[index + 1] != 'a'):
                srcCode += "8"
                babyWord = ""
            elif (babyWord == "baaaaaaaaa"):
                srcCode += "9"
                babyWord = ""

    return srcCode