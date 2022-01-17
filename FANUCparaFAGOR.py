# -*- coding: utf-8 -*-
import os

def FANUCparaFAGOR():
    #Incio do codigo
    #linha=0
    ArquivoFANUC = open("Fanuc.nc")
    linhaAtual = ArquivoFANUC.readline()
    tamanhoLinhaAtual = len(linhaAtual)
    if(tamanhoLinhaAtual>0):
        if (linhaAtual[0]=="O")or(linhaAtual[0]=="o"):
            x=0
            while (x<tamanhoLinhaAtual):
                if (linhaAtual[x]=="("):
                    linhaAtual = linhaAtual.split("(")[1]
                    linhaAtual = linhaAtual.replace(")", "")
                    linhaAtual = linhaAtual.replace("\n", "")
                    linhaAtual = "%" + linhaAtual + ",MX--,\n"
                    x=tamanhoLinhaAtual
                x+=1
    texto = linhaAtual
    while(tamanhoLinhaAtual >0):
        linhaAtual = ArquivoFANUC.readline()
        linhaAtual = linhaAtual.replace("#0", "P0")
        linhaAtual = linhaAtual.replace("#1", "P1")
        linhaAtual = linhaAtual.replace("#2", "P2")
        linhaAtual = linhaAtual.replace("#3", "P3")
        linhaAtual = linhaAtual.replace("#4", "P4")
        linhaAtual = linhaAtual.replace("#5", "P5")
        linhaAtual = linhaAtual.replace("#6", "P6")
        linhaAtual = linhaAtual.replace("#7", "P7")
        linhaAtual = linhaAtual.replace("#8", "P8")
        linhaAtual = linhaAtual.replace("#9", "P9")
        tamanhoLinhaAtual = len(linhaAtual)
        if tamanhoLinhaAtual>0:
            if (linhaAtual[0]=="("):
                linhaAtual = linhaAtual.split("(")[1]
                linhaAtual = linhaAtual.split(")")[0]
                linhaAtual = ";" + linhaAtual + "\n"
            x=0
            tamanhoLinhaAtual = len(linhaAtual)
            while (x<tamanhoLinhaAtual-1):
                if(linhaAtual[x]=="("):
                    comando=linhaAtual[0:x]
                    comentario=linhaAtual[x+1:tamanhoLinhaAtual-2]
                    linhaAtual = comando +  ";" + comentario + "\n"
                    x=tamanhoLinhaAtual+1
                x+=1
            if(linhaAtual[0]=="P"):
                linhaAtual = linhaAtual.replace("\n", "")
                linhaAtual = "("+linhaAtual
                if (linhaAtual.count(";")>0):
                    linhaAtual = linhaAtual.replace(";", ");")
                else:
                    linhaAtual += ")"
                linhaAtual+="\n"
        if tamanhoLinhaAtual>2:
            if (linhaAtual[0:2]=="IF"):
                linhaAtual = linhaAtual.replace(" ", "")
                linhaAtual = linhaAtual.replace("\n", "")
                linhaAtual = linhaAtual.replace("EQ", " EQ ")
                linhaAtual = linhaAtual.replace("GT", " GT ")
                linhaAtual = linhaAtual.replace("LT", " LT ")
                var1 = linhaAtual.split(" ")[0]
                var1 = var1.split("[")[1]
                var2 = linhaAtual.split(" ")[2]
                var2 = var2.split("]")[0]
                comp = linhaAtual.split(" ")[1]
                LBL = linhaAtual.split("GOTO")[1]
                linhaAtual = "(IF ("+var1+" "+comp+" "+var2+")GOTO N"+LBL+")\n"
        linhaAtual = linhaAtual.replace(";P6=P6-TORP0", "(P6=P6-TOR(P0))")
        linhaAtual = linhaAtual.replace(";P7=P7-TORP0", "(P7=P7-TOR(P0))")
        linhaAtual = linhaAtual.replace("G0 Z197", "G53 G00 Z-10")
        n=linhaAtual.count("COS[")
        while (n>0):
            var=linhaAtual.split("COS[")[1]
            corte=var.find("]")
            var=var[0:corte].replace("[","")
            x="COS("+var+")"
            y="COS["+var+"]"
            linhaAtual = linhaAtual.replace(y, x)
            n=linhaAtual.count("COS[")
        n=linhaAtual.count("SIN[")
        while (n>0):
            var=linhaAtual.split("SIN[")[1]
            corte=var.find("]")
            var=var[0:corte].replace("[","")
            x="SIN("+var+")"
            y="SIN["+var+"]"
            linhaAtual = linhaAtual.replace(y, x)
            n=linhaAtual.count("SIN[")
        texto += linhaAtual
    escrever = open("FAGOR.PIM", "w")
    escrever.write(texto)
    escrever.close()
    #print texto

FANUCparaFAGOR()

