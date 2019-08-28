import csv
from PIL import Image, ImageDraw, ImageFont

with open('ruta del documento csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row[0],row[1] )
        try:
            imagen = Image.open("Ruta de la imgagen")
            #elejir un tipo y tamaño de letra
            font = ImageFont.truetype("TitilliumWeb-Light.ttf",50)
            draw = ImageDraw.Draw(imagen)
            #(puntos donde empieza las letras, texto , fuente de texto, color , alineacion)
            draw.text((150, 700), row[0]+"\n"+row[1]+"\n"+row[2], font=font, fill="black", align= "left")
            #row[0] es el campo especifico que se elije en el texto
            imagen.save("nombre con el que se guarda".jpg")
        except:
            print("No ha sido posible cargar la imagen")
