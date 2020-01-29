from models.Persona import Persona
import json


persona = Persona()

persona.nombre = "pedro"
persona.apellido = "Rodriguez"
persona.edad = 30

jsonStr = json.dumps(persona.__dict__)



print(jsonStr)

leerPersonas = open('./db/persona.json', 'r')

listaPersonas = leerPersonas.read()

leerPersonas.close()


listPersons = json.loads(listaPersonas)

# personaStr = json.JSONDecoder()

personaObj = persona.__dict__

listPersons.append(personaObj)

#listPersons.append(jsonStr)

listaStr = json.dumps(listPersons)

archivoEscritura = open('./db/persona.json', 'w')
archivoEscritura.write(listaStr)
archivoEscritura.close()




