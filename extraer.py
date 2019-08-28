import csv
from PIL import Image, ImageDraw, ImageFont

with open('salida.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row[0],row[1] )
        try:
            imagen = Image.open("SER.jpeg")
            # Define tupla con región
            #caja = (95, 600, 869, 1015)
            nombre=row[0]+row[1]
            print(len(row[0])>len(row[1]))
            font = ImageFont.truetype("TitilliumWeb-Light.ttf",50)
            draw = ImageDraw.Draw(imagen)
            draw.text((150, 700), row[0]+"\n"+row[1]+"\n"+"CI:"+row[2], font=font, fill="black", align= "left")
            #print(imagen.size)
            imagen.save("Icredenciales/"+row[0]+row[1]+".jpg")
            # Obtener de la imagen original la región de la caja
            #region = imagen.crop(caja)  
            #region.show()  # Mostrar imagen de la region
            #region.size   # Mostrar tamaño de imagen final 600x400
            # Guarda la imagen obtenida con el formato JPEG.
            #region.save("region.jpg")
            # Guarda la imagen obtenida con el formato PNG.
            #region.save("region.png")
        except:
            print("No ha sido posible cargar la imagen")