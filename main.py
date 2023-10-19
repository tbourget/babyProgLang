#TJ Bourget was here

import evaluator
import lexer
import parserr
import decipher

while True:
    babyExp = input(">>> ")
    if babyExp == "poopoo":
        break
    srcCode = decipher.decipher(babyExp)
    tokSeq = lexer.tokenize(srcCode)
    rootNode = parserr.parse(tokSeq)
    result = evaluator.evaluate(rootNode)
    parserr.printTree(rootNode)
    print()
    print("The result is: ", result)

print("Now it is time to go poo poo.")

