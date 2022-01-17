# -*- coding: utf-8 -*-
import os

def FAGORparaFANUC():
    #Incio do codigo
    ArquivoFAGOR = open("Fagor.PIM")
    linhaAtual = ArquivoFAGOR.readline()
    tamanhoLinhaAtual = len(linhaAtual)
    texto = ""
    while(tamanhoLinhaAtual >0):
        if (linhaAtual[0]=="%"):
            linhaAtual = linhaAtual.replace("%", "")
            linhaAtual = linhaAtual.replace(",MX--", "")
            linhaAtual = linhaAtual.replace(",", "")
            linhaAtual = linhaAtual.replace(" ", "")
            linhaAtual = linhaAtual.replace("\n", "")
            linhaAtual = "O0001(" + linhaAtual + ")\n"
            texto = linhaAtual
        linhaAtual = ArquivoFAGOR.readline()
        linhaAtual = linhaAtual.replace("P0", "#0")
        linhaAtual = linhaAtual.replace("P1", "#1")
        linhaAtual = linhaAtual.replace("P2", "#2")
        linhaAtual = linhaAtual.replace("P3", "#3")
        linhaAtual = linhaAtual.replace("P4", "#4")
        linhaAtual = linhaAtual.replace("P5", "#5")
        linhaAtual = linhaAtual.replace("P6", "#6")
        linhaAtual = linhaAtual.replace("P7", "#7")
        linhaAtual = linhaAtual.replace("P8", "#8")
        linhaAtual = linhaAtual.replace("P9", "#9")
        n=linhaAtual.count("COS(")
        while (n>0):
            var=linhaAtual.split("COS(")[1]
            corte=var.find(")")
            var=var[0:corte].replace("(","")
            x="COS("+var+")"
            y="COS["+var+"]"
            linhaAtual = linhaAtual.replace(x, y)
            linhaAtual = linhaAtual.replace("])", "]")
            n=linhaAtual.count("COS(")
        n=linhaAtual.count("SIN(")
        while (n>0):
            var=linhaAtual.split("SIN(")[1]
            corte=var.find(")")
            var=var[0:corte].replace("(","")
            x="SIN("+var+")"
            y="SIN["+var+"]"
            linhaAtual = linhaAtual.replace(x, y)
            linhaAtual = linhaAtual.replace("])", "]")
            n=linhaAtual.count("SIN(")
        if (linhaAtual.split(" ")[0]=="(IF"):
            linhaAtual = linhaAtual.replace(" ", "")
            linhaAtual = linhaAtual.replace("(IF", "IF")
            linhaAtual = linhaAtual.replace("(", "[")
            linhaAtual = linhaAtual.replace(")", "]")
            linhaAtual = linhaAtual.replace("GOTON", "THEN GOTO")
            linhaAtual = linhaAtual.split("GOTO")[0] + "GOTO" + linhaAtual.split("GOTO")[1].replace("]", "")
        linhaAtual = linhaAtual.replace("(#", "#")
        linhaAtual = linhaAtual.replace("0)", "0")
        linhaAtual = linhaAtual.replace("1)", "1")
        linhaAtual = linhaAtual.replace("2)", "2")
        linhaAtual = linhaAtual.replace("3)", "3")
        linhaAtual = linhaAtual.replace("4)", "4")
        linhaAtual = linhaAtual.replace("5)", "5")
        linhaAtual = linhaAtual.replace("6)", "6")
        linhaAtual = linhaAtual.replace("7)", "7")
        linhaAtual = linhaAtual.replace("8)", "8")
        linhaAtual = linhaAtual.replace("9)", "9")
        tamanhoLinhaAtual = len(linhaAtual)
        if tamanhoLinhaAtual>0:
            if (linhaAtual[0]==";"):
                linhaAtual = linhaAtual.replace("\n", "")
                linhaAtual = linhaAtual.replace(";", "(") + ")\n"
            x=0
            while (x<tamanhoLinhaAtual):
                if (linhaAtual[x]==";"):
                    linhaAtual = linhaAtual.replace("\n", "")
                    linhaAtual = linhaAtual.replace(";", "(") + ")\n"
                x+=1
        linhaAtual = linhaAtual.replace("#6=#6-TOR#0)", "(#6=#6-TOR#0)")
        linhaAtual = linhaAtual.replace("#7=#7-TOR#0)", "(#7=#7-TOR#0)")
        linhaAtual = linhaAtual.replace("G53 G00 Z-10", "G0 Z197")
        texto += linhaAtual
    escrever = open("Fanuc.nc", "w")
    escrever.write(texto)
    escrever.close()
    #print texto

FAGORparaFANUC()

