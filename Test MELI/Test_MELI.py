import requests
import mysql.connector
#import json

#Conexión a la BD
cnn = mysql.connector.connect(host="localhost", user="root",
passwd="toor", database="melitest2")

#GET de los datos de la API. Hago un GET inicial para borrar la tabla
urlborra = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
databorrar = requests.get(urlborra)

if databorrar.status_code == 200:
    data = databorrar.json()
    for b in data:
        curborra = cnn.cursor()
        eliminar="""delete from clientesapi"""
        curborra.execute(eliminar)
        cnn.commit()
        curborra.close()

#GET de los datos de la API
url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
data = requests.get(url)

if data.status_code == 200:#Valida que la respuesta HTTP sea exitosa
    data = data.json()
    for e in data:
        cur = cnn.cursor()
        val = (e['fec_alta'], e['user_name'],e['codigo_zip'], e['credit_card_num'], e['credit_card_ccv'], e['cuenta_numero'], e['direccion'], e['geo_latitud'], e['geo_longitud'], e['color_favorito'], e['foto_dni'], e['ip'], e['auto'], e['auto_modelo'], e['auto_tipo'], e['auto_color'], e['cantidad_compras_realizadas'], e['avatar'], e['fec_birthday'], e['id'])
        sql="""INSERT INTO clientesapi (fec_altabd,user_namebd,codigo_zipbd,credit_card_numbd,credit_card_ccvbd,cuenta_numerobd,direccionbd,geo_latitudbd,geo_longitudbd,color_favoritobd,foto_dnibd,ipbd,autobd,auto_modelobd,auto_tipobd,auto_colorbd,cantidad_compras_realizadasbd,avatarbd,fec_birthdaybd,idbd) values (%s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cur.execute(sql,val)
        cnn.commit()
        #cnn.close()
        print ("Fecha de alta: ", e['fec_alta'])
        print ("Nombre: ", e['user_name'])
        print ("Codigo ZIP: ", e['codigo_zip'])
        #print ("Numero tarjeta de credito: ", e['credit_card_num'])
        print ("Numero tarjeta de credito: ****-****-****-", e['credit_card_num'] [-5:])#La TC la imprimo enmascarada
        print ("Numero de CCV: ", e['credit_card_ccv'])
        #print ("Numero de cuenta: ", e['cuenta_numero'])
        print ("Numero de cuenta: ****-", e['cuenta_numero'] [-4:])#La cuenta también la imprimo enmascarada
        print ("Direccion: ", e['direccion'])
        print ("Geo latitud: ", e['geo_latitud'])
        print ("Geo longitud: ", e['geo_longitud'])
        print ("Color favorito: ", e['color_favorito'])
        print ("Foto DNI: ", e['foto_dni'])
        print ("IP: ", e['ip'])
        print ("Auto: ", e['auto'])
        print ("Modelo auto: ", e['auto_modelo'])
        print ("Tipo de auto: ", e['auto_tipo'])
        print ("Color del auto: ", e['auto_color'])
        print ("Cantidad transacciones: ", e['cantidad_compras_realizadas'])
        print ("Avatar: ", e['avatar'])
        print ("Fecha de cumpleanos: ", e['fec_birthday'])
        print ("Id:: ", e['id'])
        print ("")