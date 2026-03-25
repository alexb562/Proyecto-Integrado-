import serial
import csv
import os
from datetime import datetime

PUERTO = "/dev/tty.usbmodem141401"
BAUDIOS = 9600
ARCHIVO_CSV = "datos_sensores.csv"
CAMPOS = ["timestamp", "sensor", "valor"]


def parsear_linea(linea):
    datos = {}
    if "BPM:" in linea:
        partes = linea.split(":")
        if len(partes) == 2:
            datos["sensor"] = "BPM"
            datos["valor"] = partes[1].strip()
    return datos


def inicializar_csv():
    if not os.path.exists(ARCHIVO_CSV) or os.path.getsize(ARCHIVO_CSV) == 0:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()


def guardar_csv(registro):
    with open(ARCHIVO_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writerow(registro)


def main():
    inicializar_csv()

    try:
        ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
        print(f"Escuchando {PUERTO}")

        while True:
            linea = ser.readline().decode("utf-8", errors="ignore").strip()

            if linea:
                print(f"{PUERTO} -> {linea}")
                datos = parsear_linea(linea)

                if "sensor" in datos and "valor" in datos:
                    registro = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "sensor": datos["sensor"],
                        "valor": datos["valor"]
                    }
                    guardar_csv(registro)
    except KeyboardInterrupt:
        print("Programa detenido")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()


main()
