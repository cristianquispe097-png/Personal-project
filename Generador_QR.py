import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

url_to_encode = input("Ingrese URL, dirección, o pagina")
api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url_to_encode}"

response = requests.get(api_url)
if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    img.save("qr_generado.png")
    titulo_de_QR=input("Ingrese titulo de QR")
    
    plt.figure(figsize=(4,4))
    plt.imshow(img)
    plt.axis('off')
    plt.title(titulo_de_QR, fontsize=10)
    plt.show()
    print("QR generado exitosamente.")
else:
    print("Error al generar el QR mediante API.")
