# Global Trade Excel Analysis

Análisis de oportunidades de comercio exterior usando Excel avanzado 
(Power Pivot, DAX), automatización con Python, y asistencia de IA — 
segunda pieza de una serie de 4 proyectos sobre el mismo caso de negocio.

## Problema de negocio

¿Qué países muestran mayor apertura comercial y crecimiento sostenido en 
comercio exterior durante la última década, y cuáles representan mayor 
riesgo de caída reciente?

## Fuente de datos

Mismo dataset del proyecto "Global Trade Opportunities" (Power BI): 
15 países, 4 indicadores de comercio exterior, Banco Mundial, 2015-2024.

## Arquitectura del proyecto


- **Power Pivot**: modelo de datos con medidas DAX personalizadas 
  (Valor Total, Valor Promedio, Variación YoY, País con Mayor Caída).
- **Python (xlwings)**: automatización de la actualización de datos y 
  lectura de resultados directamente desde el modelo de Excel.
- **ChatGPT**: asistencia en la generación de una medida DAX avanzada, 
  adaptada posteriormente al modelo de datos real del proyecto.
- **Excel**: panel ejecutivo con tabla dinámica, gráfico dinámico de 
  doble eje, y segmentadores interactivos por año e indicador.

## Estructura del repositorio

├── data_raw/ # Dataset limpio (reutilizado del proyecto Power BI)
├── data_processed/ # Datos procesados específicos si aplica
├── excel/ # Archivo de Excel y script de automatización
├── docs/ # Documentación adicional
├── outputs/ # Capturas y elementos generados
└── README.md


## Cómo correrlo

1. Clonar el repositorio.
2. Abrir `excel/global_trade_excel_analysis.xlsx` en Excel (requiere 
   complemento Power Pivot activado).
3. Para ejecutar la automatización: `py excel/refresh_data.py` (requiere 
   Python con `xlwings` instalado en Windows, y el archivo Excel abierto).

## Insights principales

1. **Colombia registró la mayor caída porcentual en comercio exterior 
   durante 2024** entre los 15 países analizados, identificada mediante 
   una medida DAX asistida por IA y validada con los datos reales del 
   modelo.
2. **Alemania, Corea del Sur y México** lideran en magnitud de comercio 
   exterior como % del PIB a lo largo de la década.
3. La automatización con Python confirma que el análisis es reproducible 
   y escalable, sin depender de actualización manual constante.
4. El uso de IA (ChatGPT) para generar fórmulas DAX requiere siempre 
   validación y adaptación al modelo de datos real — un ejemplo concreto 
   de esto quedó documentado en el proceso.

## Recomendación

Monitorear de cerca a Colombia por su caída reciente en apertura 
comercial, y evaluar oportunidades de expansión prioritariamente en 
economías con comportamiento estable y alto volumen, como Alemania y 
Corea del Sur.

## Autor

Jason Daniel Martínez — [LinkedIn](http://www.linkedin.com/in/jasondanielmartinezcastro)