import requests
import json
from datetime import datetime

def extraer_clima_estable():
    # Coordenadas exactas de Santa Rosa, Misiones, Paraguay
    latitud = -26.8667
    longitud = -56.8500
    
    # Pedimos los sensores actuales y los datos por hora
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m,rain,surface_pressure,uv_index&hourly=temperature_2m,relative_humidity_2m,rain&timezone=America%2FAsuncion&forecast_days=1"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() 
        datos = respuesta.json()
        
        clima_actual = datos["current"]
        clima_por_hora = datos["hourly"]
        
        resultado = {
            "ciudad": "Santa Rosa, Misiones",
            "fecha_actualizacion": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "actual": {
                "temperatura": clima_actual['temperature_2m'],
                "humedad": clima_actual['relative_humidity_2m'],
                "viento_velocidad": clima_actual['wind_speed_10m'],
                "viento_direccion": clima_actual['wind_direction_10m'],
                "lluvia": clima_actual['rain'],
                "presion": clima_actual['surface_pressure'],
                "uv": clima_actual['uv_index']
            },
            "historial": {
                "horas": clima_por_hora['time'],
                "temperatura": clima_por_hora['temperature_2m'],
                "humedad": clima_por_hora['relative_humidity_2m'],
                "lluvia": clima_por_hora['rain']
            }
        }
        
        with open("clima_santarosa.json", "w", encoding="utf-8") as archivo:
            json.dump(resultado, archivo, ensure_ascii=False, indent=4)
            
        print("✅ Datos guardados con éxito en 'clima_santarosa.json'")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    extraer_clima_estable()