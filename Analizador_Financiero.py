#Analizador_Financiero
import yfinance
import pandas as pd
import numpy as np

def ejecutar_analisis():
    # 1. Entrada de usuario
    print("--- Analizador de Mercado Pro ---")
    ticker_input = input("Ingrese el símbolo de la acción (ej: MELI.BA, AAPL): ").upper()
    
    try:
        # 2. Descarga de datos
        print(f"Descargando datos para {ticker_input}...")
        data = yfinance.Ticker(ticker_input).history(period="6mo")
        
        if data.empty:
            print("Error: No se encontraron datos. Verifique el símbolo.")
            return

        # 3. Limpieza de zona horaria para Excel
        data.index = data.index.tz_localize(None)
        cierre = data['Close']

        # 4. Cálculos Financieros
        valor_max = round(cierre.max(), 2)
        valor_mi = round(cierre.min(), 2)
        valor_medio = round(cierre.mean(), 2)
        
        # Variación y Tendencia
        variacion_total = ((cierre.iloc[-1] - cierre.iloc[0]) / cierre.iloc[0]) * 100
        tendencia = "ALCISTA" if variacion_total > 0 else "BAJISTA"
        
        # Volatilidad
        data['Retornos'] = data['Close'].pct_change()
        volatilidad = round(data['Retornos'].std() * 100, 2)

        # 5. Creación del Resumen
        resumen_dict = {
            "Métrica": ["Acción", "Máximo", "Mínimo", "Promedio", "Variación %", "Tendencia", "Volatilidad Diaria"],
            "Valor": [ticker_input, valor_max, valor_mi, valor_medio, f"{round(variacion_total, 2)}%", tendencia, f"{volatilidad}%"]
        }
        df_resumen = pd.DataFrame(resumen_dict)

        # 6. Exportar a Excel
        nombre_archivo = f"Reporte_{ticker_input}.xlsx"
        with pd.ExcelWriter(nombre_archivo) as writer:
            data.to_excel(writer, sheet_name='Datos_Historicos')
            df_resumen.to_excel(writer, sheet_name='Analisis', index=False)

        print(f"\n¡Éxito! El reporte '{nombre_archivo}' ha sido generado.")
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_analisis()