g = open('grafica1.json')
f = open('grafica1.js', 'a')
f.truncate(0)
f.write('var grafica1 = '+g.read())
f.close()
''' Algoritmo'''
'''
1. leo el archivo que el json 
2. leo en modo appdenn el js
3. borro lo que haya en el js
4. escribo lo que necesito
5. cierro el file 
'''