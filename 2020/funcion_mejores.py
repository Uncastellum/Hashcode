
def insertOrd(vector, dato, puntucion, long):

	i = 0
	encontrado = False
	while i < long and not encontrado:
	
		if puntuacion[dato] >= puntuacion[i]:
		
			vector.insert(i)
			encontrado = True
			
		else:
			
			i+=1
			
	return vector

def buscarXbest(libros, puntuacion, total):

	len = 0
	res = []
	
	for i in libros:
	
		if len == 0:
		
			res.append(i)
			len += 1
			
		else:
			
			insertOrd(res, i, puntuacion, len)
			len += 1
			
			if len >= total*3:
				
				return res
	
	return res
			