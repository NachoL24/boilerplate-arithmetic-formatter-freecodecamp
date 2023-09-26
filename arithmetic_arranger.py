def arithmetic_arranger(problems, solucion = False):
  cadenaSuperior=''
  cadenaInferior=''
  lineaPunteada=''
  contador=0
  cadenaTotal=''
  cadenaResultados=''
  long=0
  if (str(problems).isupper()) or (str(problems).islower()):
    return 'Error: Numbers must only contain digits.'
  if len(problems) < 6: 
    for operacion in problems:
      #print(operacion)
      if(contador>0) and (contador < len(problems)):
        cadenaSuperior=cadenaSuperior+' '*4
        cadenaInferior=cadenaInferior+' '*4
        lineaPunteada=lineaPunteada+' '*4
        cadenaResultados=cadenaResultados+' '*4
      operador=0
      operacion = operacion.replace(" ","")
      operador = operacion.find('+')
      if (operador > 0):
        #parte positiva
        terminos = operacion.split('+')
        if (not (terminos[0].isnumeric())) or (not (terminos[1].isnumeric())):
          return "Error: Operator must be '+' or '-'."
        if (len(terminos[0])> 4) or (len(terminos[1])>4):
          return 'Error: Numbers cannot be more than four digits.'
        if len(terminos[0]) > len(terminos[1]):
          #caso en que el primer termino es de mayor tamaño
          cadenaSuperior=cadenaSuperior+'  '+terminos[0]
          cadenaInferior=cadenaInferior+'+ '+' '*(len(terminos[0])-len(terminos[1]))+terminos[1]
          long=len(terminos[0])+2
          lineaPunteada=lineaPunteada+'-'*long
        elif len(terminos[0]) == len(terminos[1]):
          #caso en que son iguales de tamaño los terminos
          cadenaSuperior=cadenaSuperior+'  '+terminos[0]
          cadenaInferior=cadenaInferior+'+ '+terminos[1]
          long=len(terminos[0])+2
          lineaPunteada=lineaPunteada+'-'*long
        else:
          #caso en el que el segundo termino es mayor
          cadenaSuperior=cadenaSuperior+'  '+' '*(len(terminos[1])-len(terminos[0]))+terminos[0]
          cadenaInferior=cadenaInferior+'+ '+terminos[1]
          long=len(terminos[1])+2
          lineaPunteada=lineaPunteada+'-'*long
        #resultado
        res=str(int(terminos[0])+int(terminos[1]))
        cadenaResultados=cadenaResultados+' '*(long-len(res))+res
      else:
        #parte negativa
        terminos = operacion.split('-')
        if (not (terminos[0].isnumeric())) or (not (terminos[1].isnumeric())):
          return "Error: Operator must be '+' or '-'."
        if (len(terminos[0])> 4) or (len(terminos[1])>4):
          return 'Error: Numbers cannot be more than four digits.'
        if len(terminos[0]) > len(terminos[1]):
          #caso en que el primer termino es de mayor tamaño
          cadenaSuperior=cadenaSuperior+'  '+terminos[0]
          cadenaInferior=cadenaInferior+'- '+' '*(len(terminos[0])-len(terminos[1]))+terminos[1]
          long=len(terminos[0])+2
          lineaPunteada=lineaPunteada+'-'*long
        elif len(terminos[0]) == len(terminos[1]):
          #caso en que son iguales de tamaño los terminos
          cadenaSuperior=cadenaSuperior+'  '+terminos[0]
          cadenaInferior=cadenaInferior+'- '+terminos[1]
          long=len(terminos[0])+2
          lineaPunteada=lineaPunteada+'-'*long
        else:
          #caso en el que el segundo termino es mayor
          cadenaSuperior=cadenaSuperior+'  '+' '*(len(terminos[1])-len(terminos[0]))+terminos[0]
          cadenaInferior=cadenaInferior+'- '+terminos[1]
          long=len(terminos[1])+2
          lineaPunteada=lineaPunteada+'-'*long
        res=str(int(terminos[0])-int(terminos[1]))
        cadenaResultados=cadenaResultados+' '*(long-len(res))+res
      contador += 1
    if solucion == False:
      cadenaTotal = cadenaSuperior+'\n'+cadenaInferior+'\n'+lineaPunteada
    else:
      cadenaTotal = cadenaSuperior+'\n'+cadenaInferior+'\n'+lineaPunteada+'\n'+cadenaResultados
  else:
    cadenaTotal = 'Error: Too many problems.'
 # return arranged_problems
  return cadenaTotal