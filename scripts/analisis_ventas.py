# analisis_ventas.py
# Propósito: Analizar indicadores de ventas del dataset simulado.
# Se usan rutas relativas para garantizar reproducibilidad en Colab.

import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar dataset desde /datos (ruta relativa para reproducibilidad)
df = pd.read_csv('datos/ventas.csv')
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

# ---- INDICADORES BÁSICOS ----
# Métricas clave para evaluar el desempeño comercial
col = [c for c in df.columns if 'amount' in c or 'sales' in c][-1]
print(f'Ventas totales: ${df[col].sum():,.2f}')
print(f'Promedio diario: ${df[col].mean():,.2f}')
print(f'Máximo: ${df[col].max():,.2f}  |  Mínimo: ${df[col].min():,.2f}')

# ---- GRÁFICO DE EVOLUCIÓN ----
os.makedirs('resultados', exist_ok=True)
plt.figure(figsize=(10, 5))
plt.plot(df[col].values, color='steelblue', linewidth=2)
plt.title('Evolución de Ventas', fontsize=14, fontweight='bold')
plt.xlabel('Día')
plt.ylabel('Monto ($)')
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png', dpi=150)
plt.show()
print('Gráfico guardado en resultados/grafico_ventas.png')
