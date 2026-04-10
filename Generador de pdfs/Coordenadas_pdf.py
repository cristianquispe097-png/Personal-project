#!pip install pdfplumber
import pdfplumber

archivo = "My Project.pdf"
paginas=int(input("Ingrese el número de páginas a analizar: "))

with pdfplumber.open(archivo) as pdf:
    page = pdf.pages[paginas]  # N° de página
    palabras = page.extract_words()
    palabras_buscar = input("Ingrese palabras a buscar separadas por coma: ").split(",")
    palabras_buscar = [p.strip().lower() for p in palabras_buscar]
    coords = []
    for palabra in palabras:
        if palabra["text"].lower() in palabras_buscar:
            coords.append((palabra["text"], palabra["x0"], palabra["top"]))
