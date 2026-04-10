#  Generando Archivos PDF
# * Crear pdf
# * Definir el tipo de letra
# * Agregar una imagen de fondo
# * Definir las coordenadas para cada campo
# * Se asigna una imagen de fondo a usar como plantilla
# * Llenado el doc
# * Guardar el entregable

detalles_proceso=input("Pasos incluidos en el proceso")
proyecto=input("Escriba Nombre Proyecto")
Horas_estimadas=input("Escriba HS estimadas dedicadas al proyecto")
valor_Hora=input("¿Cual es el valor Hora?")
Plazo_Estimado=input("¿Cual es el plazo estiado?")
Valor_Total=int(Horas_estimadas)*int(valor_Hora)
imagen=input("Escriba el nombre de la imagen a usar como plantilla (ej: Presupuesto.png)")
# !pip install fpdf 
# es una libreria para crear pdf
from fpdf import FPDF  
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image(imagen,0,0)
pdf.text(204,150,detalles_proceso)
pdf.text(115,145, proyecto)
pdf.text(115,160, Horas_estimadas)
pdf.text(115,175, valor_Hora)
pdf.text(115,190, Plazo_Estimado)
pdf.text(115,205, str(Valor_Total))

pdf.output("Presupuesto2026.pdf")