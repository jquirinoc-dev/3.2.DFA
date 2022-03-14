from wsgiref import headers
from tabulate import tabulate

letras = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',"_")
numeros = ('0','1','2','3','4','5','6','7','8','9')
operators = ('=','+','-','/','^','*')
parentesis = ('(',')')
punto = "."

table = [["Token", "Type"]]

lines = []

with open('expresiones.txt') as f:
    newline_break = ""
    for readline in f:
        line_strip = readline.strip()
        line_strip = line_strip.replace(" ", "")
        line_strip = line_strip.lower()
        lines.append(line_strip)


def checkingOperators(string, j):
    
    tokenType = ""
    out = ""

    if string[j] == "+":
        out += "+"
        tokenType = "Suma"
    elif string[j] == "=":
        out += "="
        tokenType = "Asignacion"
    elif string[j] == "-":
        out += "-"
        tokenType = "Resta"
    elif string[j] == "/":
        if string[j + 1] == "/":
            out += string[j:]
            tokenType = "Comentario"
            j = len(string)
        else:
            out += "/"
            tokenType = "Division"
    elif string[j] == "^":
        out += "^"
        tokenType = "Potencia"
    elif string[j] == "*":
        out += "*"
        tokenType = "Multiplicacion"
    
    tmpList = [out, tokenType]
    table.append(tmpList)
    
    return j
   
def checkingNumbers(string, j):

    tokenType = "Entero"

    out = string[j]
    j += 1
    
    while j <= len(string) - 1 and string[j] in numeros:
        out += string[j]
        j += 1
    

    if j < len(string) - 1 and string[j] == punto:
        tokenType = "Real"
        out += "."
        j += 1

        while j <= len(string) - 1 and string[j] in numeros:
            out += string[j]
            j += 1
        
    if j < len(string) - 1 and string[j] == "e":
        out += string[j]
        j += 1

        if j < len(string) - 1 and string[j] == "-":
            out += "-"
            j += 1

        while j <= len(string) - 1 and string[j] in numeros:
            out += string[j]
            j += 1
    j-= 1
            

    
    """ print(out) """
    tmpList = [out, tokenType]
    table.append(tmpList)
    return j

def checkingParethesis(string, j):
    tokenType = ""
    out = ""

    if string[j] == "(":
        out += "("
        tokenType = "Parentesis de apertura"
    elif string[j] == ")":
        out += ")"
        tokenType = "Parentesis de cierre"
    
    tmpList = [out, tokenType]
    table.append(tmpList)
    return j

def checkingVariables(string, j):
    
    tokenType = "Variable"

    out = string[j]
    j += 1
    
    while j <= len(string) - 1 and string[j] in letras or string[j] in numeros:
        out += string[j]
        j += 1
    
    j -= 1

    tmpList = [out, tokenType]
    table.append(tmpList)
    return j



def main():

    for i in range(len(lines)):
        j = 0
        while j <= len(lines[i]) - 1:
        
            
            if lines[i][j] in letras:
                j = checkingVariables(lines[i], j)

            elif lines[i][j] in operators:
                
                if lines[i][j] == "-" and lines[i][j + 1] in numeros and lines[i][j - 1] not in numeros and lines[i][j - 1] not in letras:
                    j = checkingNumbers(lines[i], j)
                else:
                    j = checkingOperators(lines[i], j)

            elif lines[i][j] in numeros:
                j = checkingNumbers(lines[i], j)

            elif lines[i][j] in parentesis:
                j = checkingParethesis(lines[i], j)
            
            j += 1


    print(tabulate(table, headers="firstrow"))


main()