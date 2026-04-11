# !pip install xlsxwriter
# !pip install pandas 
# !pip install openpyx1
# !pip install plotly
# !pip install nbformat
# !pip install openpyxl
import pandas as pd #Definir con que se empieza a trabajar
import matplotlib.pyplot as plt
print("--- Analizador de Archivos Excel ---")
ticker_input = input("Ingrese el nombre del archivo (ej: ventas): ") + ".xlsx"

try:
     # 0. Cargar datos
    archivo_origen = ticker_input  # Reemplaza con tu archivo de datos"
    data = pd.read_excel(archivo_origen)
    print("Columnas encontradas en el archivo:", data.columns.tolist())
    data.columns = [col.strip().title() for col in data.columns]
   # 1. Ingreso de columnas a analizar
    columnas_input = input("Ingrese columnas a analizar (ej: Clave Producto, Clave Vendedor): ") #Son los parametros de agrupamiento
    columnas = [col.strip() for col in columnas_input.split(",")]

    # 2. Validación de columnas contra las reales del archivo
    columnas_validas = data.columns.tolist()
    for col in columnas:
        if col not in columnas_validas:
            raise ValueError(f"La columna '{col}' no existe en los datos. Columnas válidas: {columnas_validas}")

    # 3. Definir métricas numéricas a calcular
    metricas = {
        'Costo': 'sum',
        'Utilidad': 'sum',
        'Ingresos': 'sum',
        'Cantidad': 'sum',
        "Ventas": "sum"
    }
    metricas_validas = {}
    for k, v in metricas.items():
        if k in data.columns:
            metricas_validas[k] = v

    # 4. Agrupación y cálculos
    df_resumen = data.groupby(columnas).agg(metricas_validas).reset_index()

    # Cálculos derivados
    if 'Costo' in df_resumen.columns and 'Utilidad' in df_resumen.columns:
        df_resumen['Margen Utilidad (%)'] = df_resumen['Utilidad'] / df_resumen['Costo'] * 100
        df_resumen['Balance'] = df_resumen['Utilidad'] - df_resumen['Costo']

    if 'Ingresos' in df_resumen.columns:
        total_ingresos = df_resumen['Ingresos'].sum()
        df_resumen['Participación (%)'] = df_resumen['Ingresos'] / total_ingresos * 100

    # 5. Gráfico de tendencia (ejemplo: evolución de ingresos por fecha si existe)
    if 'Fecha' in data.columns and 'Ingresos' in data.columns:
        tendencia = data.groupby('Fecha')['Ingresos'].sum()
        plt.figure(figsize=(8,5))
        tendencia.plot(marker='o')
        plt.xlabel("Fecha")
        plt.ylabel("Ingresos")
        plt.title("Tendencia de Ingresos en el tiempo")
        plt.tight_layout()
        plt.savefig("grafico_tendencia.png")

    # 6. Guardar resultados en Excel
    nombre_archivo = f"Reporte_{ticker_input}"
    with pd.ExcelWriter(nombre_archivo, engine='xlsxwriter') as writer:
        data.to_excel(writer, sheet_name='Datos_Solicitados', index=False)
        df_resumen.to_excel(writer, sheet_name='Analisis', index=False)

        # Insertar gráfico si fue generado
        if 'Fecha' in data.columns and 'Ingresos' in data.columns:
            workbook = writer.book
            worksheet = workbook.add_worksheet('Graficos')
            worksheet.insert_image('B2', 'grafico_tendencia.png')

    print(f"\n¡Éxito! El reporte '{nombre_archivo}' ha sido generado.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
