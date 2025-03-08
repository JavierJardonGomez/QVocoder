import argparse
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def load_audio(filepath, sr=22050):
    y, sr = librosa.load(filepath, sr=sr)
    return y, sr

def plot_waveform(y, sr, title="Forma de Onda"):
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title(title)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid()
    plt.show()

def plot_spectrogram(y, sr, title="Espectrograma de Mel"):
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mel_spec_db, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title(title)
    plt.show()

def select_file():
    root = tk.Tk()
    root.withdraw()  # No mostrar la ventana principal
    file_path = filedialog.askopenfilename(title="Seleccionar archivo WAV", filetypes=[("Archivos WAV", "*.wav")])
    return file_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualizar la forma de onda y espectrograma de un archivo WAV.")
    parser.add_argument("wav_path", type=str, nargs='?', help="Ruta del archivo WAV a visualizar")
    args = parser.parse_args()

    # Si no se pasa el archivo como argumento, se abrirá el explorador de archivos
    if args.wav_path is None:
        wav_path = select_file()
    else:
        wav_path = args.wav_path

    if wav_path:  # Verificar que se haya seleccionado un archivo
        # Cargar el audio y mostrar las gráficas
        y, sr = load_audio(wav_path)
        plot_waveform(y, sr, title="Forma de Onda de " + wav_path)
        plot_spectrogram(y, sr, title="Espectrograma de " + wav_path)
    else:
        print("No se ha seleccionado ningún archivo.")
