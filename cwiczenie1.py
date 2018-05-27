import os
import os.path
import subprocess
import sys
import mpmath
from sympy.combinatorics.prufer import Prufer
from PIL import Image
sys.modules['sympy.mpmath'] = mpmath

def assign_code(nodes, label, result, prefix = ''):    
    childs = nodes[label]     
    tree = {}
    if len(childs) == 2:
        tree['0'] = assign_code(nodes, childs[0], result, prefix)
        tree['1'] = assign_code(nodes, childs[1], result, prefix)     
        return tree
    else:
        result[label] = prefix
        return label

def Huffman_code(_vals):    
    vals = _vals.copy()
    nodes = {}
    for n in vals.keys():
        nodes[n] = []

    while len(vals) > 1:
        s_vals = sorted(vals.items(), key=lambda x:x[1]) 
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1+a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1+a2] = [a1, a2]        
    code = {}
    root = a1+a2
    tree = {}
    tree = assign_code(nodes, root, code)    
    return code, tree

#wyzerowanie numerowania wierzchołków
def set_globvar_to_zero():
    global j   
    j = 0

j = 0
set_globvar_to_zero()
listValue = []
prefixCode = {}
graphStructure = []
def draw_tree(tree, val, prefix = ''):
    global j
    global listValue
    j += 1  
    if isinstance(tree, str):    
        descr = '%s [label="%s %s", fontsize=16, fontcolor=blue, width=2, shape=box];\n'%(j-1, j-1, tree)
        prefixCode[prefix] = j-1
        listValue.append(tree)	
    else: 
        descr = '%s [label="%s"];\n'%(j-1, j-1) #tu był prefix
        prefixCode[prefix] = j-1
        for child in tree.keys(): 
            descr += draw_tree(tree[child], j-1, prefix = prefix+child)
            descr += '%s -> %s;\n'%(prefixCode[prefix],prefixCode[prefix+child])
            graphStructure.append([prefixCode[prefix],prefixCode[prefix+child]])
    return descr

def program():
    j = 0
    option = input("Wpisz opcję(1 - Drzewo Huffmana + Kodowanie Prufera lub 2 - Dekodowanie Prufera lub 3 - Wyjście): ")
    if option == "1":
        while True:
            fileWithInputData = input("Plik z tekstem wejściowym: ") 
            if os.path.exists(fileWithInputData):   
                file_object  = open(fileWithInputData, "r")
                break
            else:
                print ("Plik nie istnieje, podaj inną scieżkę!")
                continue
        word = file_object.read()
        dictionary = {}
        for c in word:
            if( c in dictionary):
                dictionary[c] += 1
            else:
                dictionary[c] = 1

        code, tree = Huffman_code(dictionary)

        nameOfGraphFile = input("Ścieżka do grafu wyjściowego - bez rozszerzenia: ")  
        set_globvar_to_zero()
        with open(nameOfGraphFile + ".dot",'w') as f:
            f.write('digraph G {\n')
            f.write(draw_tree(tree, 0))
            f.write('}')      
        subprocess.call('dot -Tpng '+nameOfGraphFile+'.dot -o '+nameOfGraphFile+'.png', shell=True)
        j = 0
        a = Prufer.to_prufer(graphStructure,len(graphStructure)+1)
        
        nameOfFile = input("Ścieżka do pliku wyjsciowego: ")
        file = open(nameOfFile, "w")
        first = "0"
        second = ""
        third = ""
        for x in a:
            second = second + str(x) + " "
        for c in listValue:  
            third = third + str(c) + " "
        lines = [first,"\n",second,"\n",third]    
        file.writelines(lines)
        file.close()
        f = Image.open(nameOfGraphFile+".png").show()
        program()
    elif option == "2":   
        while True:
            fileWithInputDataMode2 = input("Ścieżka do pliku z kodem Prufera: ") 
            if os.path.exists(fileWithInputDataMode2):   
                file_object  = open(fileWithInputDataMode2, "r")
                break
            else:
                print ("Plik nie istnieje, podaj inną scieżkę!")
                continue
        pruferVert = []   
        pruferLet = []
        
        for i, line in enumerate(file_object):
            if i == 1:
                pruferNumbers = line.split(" ")
                for z in pruferNumbers:
                    pruferVert.append(z)
            elif i == 2:
                pruferLetters = line.split(" ")           
                for z in pruferLetters:
                    pruferLet.append(z)
            elif i > 2:
                break

        for line in pruferVert:
            if line == " " or line == '\n':
                pruferVert.remove(line)
        for line in pruferLetters:
            if line == " " or line == '\n' or line == '':
                pruferLetters.remove(line)
        #print(pruferLetters)
        #print(pruferVert)
        Prufer_list = [int(i) for i in pruferVert]
        firstPrufferLetter = pruferLetters[0]
        a = Prufer.to_tree(Prufer_list)
        newStr = "digraph G {\n"
        numberLetterDictionary = []
        for x in a:
            numberLetterDictionary.append(str(x[0]))
        for x in a:
            newStr += str(x[0]) + " -> "
            newStr += str(x[1]) + "\n"   
            if str(x[1]) not in numberLetterDictionary:
                newStr += '%s [label="%s %s", fontsize=16, fontcolor=blue, width=2, shape=box];\n'%(str(x[1]), str(x[1]), firstPrufferLetter) + "\n"
                try:
                    pruferLetters.pop(0)
                    firstPrufferLetter = pruferLetters[0]
                except IndexError:    
                    pass
        newStr+="}"
        nameOfGraphFilePrufer = input("Podaj sciezke gdzie ma powstac graf - bez rozszerzenia: ")  
        with open(nameOfGraphFilePrufer + ".dot",'w') as f:
            f.write(newStr)      
        subprocess.call('dot -Tpng '+nameOfGraphFilePrufer+'.dot -o '+nameOfGraphFilePrufer+'.png', shell=True)
        f = Image.open(nameOfGraphFilePrufer+".png").show()
        program()
    elif option == "3":
        sys.exit()
    else:
        print("Coś poszło nie tak, proszę wybrać 1 lub 2")
        program()
        
program()
