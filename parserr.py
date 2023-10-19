#TJ Bourget was here

import lexer

class treeNode:
    def __init__(self,type,value,precedence):
        self.type = type
        self.value = value
        self.precedence = precedence
    parent = None
    lChild = None
    rChild = None

def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    return precedence

def createTreeNodeList(tokSeq):
    treeNodeList = []
    precBoost = 0;

    for index in range(len(tokSeq)):
        if(tokSeq[index].type == "MINUS"):
            if(index == 0):
                tokSeq.remove(tokSeq[index])
                tokSeq.insert(index, lexer.token("UNARYMINUS", '~'))
            elif(tokSeq[index-1].type != "NUMBER"):
                tokSeq.remove(tokSeq[index])
                tokSeq.insert(index, lexer.token("UNARYMINUS", '~'))

    for tok in tokSeq:
        if (tok.type == "UNARYMINUS"):
            index = tokSeq.index(tok)
            tokSeq.remove(tokSeq[index])
            tokSeq.insert(index, lexer.token("LPAREN", '('))
            tokSeq.insert(index + 1, lexer.token("LPAREN", '('))
            tokSeq.insert(index + 2, lexer.token("NUMBER", '0'))
            tokSeq.insert(index + 3, lexer.token("MINUS", '-'))
            tokSeq.insert(index + 4, lexer.token("NUMBER", '1'))
            tokSeq.insert(index + 5, lexer.token("RPAREN", ')'))
            tokSeq.insert(index + 6, lexer.token("MULTIPLICATION", '*'))
            tokSeq.insert(index + 7, lexer.token("RPAREN", ')'))

    for token in tokSeq:

        if(token.type == "LPAREN"):
            precBoost += 4
        elif(token.type == "RPAREN"):
            precBoost -= 4
        else:
            if(token.type != "NUMBER"):
                newNode = treeNode(token.type, token.value, getPrecedence(token.type)+precBoost)
            else:
                newNode = treeNode(token.type, token.value, getPrecedence(token.type))
            treeNodeList.append(newNode)
    return treeNodeList

def parse(tokSeq):
    rootNode = None
    treeNodeList = createTreeNodeList(tokSeq)
    parsing(treeNodeList)
    rootNode = findRoot(treeNodeList)
    return rootNode

def parsing(treeNodeList):
    if(len(treeNodeList) == 1): return treeNodeList
    dummyNode = treeNode("DUMMY", "", 0)
    treeNodeList.insert(0,dummyNode)
    treeNodeList.append(dummyNode)

    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
        if node.type == "NUMBER":
            lOp = treeNodeList[index - 1]
            rOp = treeNodeList[index + 1]
            if rOp.precedence > lOp.precedence:
                rOp.lChild = node
                node.parent = rOp
                if lOp.type != "DUMMY":
                    lOp.rChild = rOp
                    rOp.parent = lOp
            else:
                lOp.rChild = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    while lOp.parent != None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent
                    if lOp.parent != None:
                        lOp.parent.rChild = rOp
                        rOp.parent = lOp.parent
                    rOp.lChild = lOp
                    lOp.parent = rOp

def findRoot(treeNodeList):
    rootNode = None
    for node in treeNodeList:
        if node.parent == None and node.type != "DUMMY":
            rootNode = node
            break
    return rootNode

def printTree(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        print(rootNode.value, end="")
    else:
        print("(",end="")
        printTree(rootNode.lChild)
        print(rootNode.value,end="")
        printTree(rootNode.rChild)
        print(")",end="")