import librosa
import os
import soundfile as sf

def resample_audio(input_dir, output_dir, target_sr=22050):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Recorre todos los archivos .wav en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.wav'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Cargar el archivo de audio con la frecuencia de muestreo original
            audio, sr = librosa.load(input_path, sr=None)  # sr=None carga el archivo con su SR original

            # Verifica si la frecuencia de muestreo es diferente de la deseada
            if sr != target_sr:
                print(f"Resampling {filename} from {sr} Hz to {target_sr} Hz")
                
                # Cambiar la frecuencia de muestreo
                audio_resampled = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)

                # Guardar el audio con la nueva frecuencia de muestreo
                sf.write(output_path, audio_resampled, target_sr)

            else:
                # Si ya tiene la frecuencia deseada, solo copiarlo
                print(f"Skipping {filename}, already at {target_sr} Hz")
                # Si lo deseas, puedes copiar los archivos sin cambios:
                # shutil.copy(input_path, output_path)

# Especifica el directorio de entrada y salida
input_directory = r'D:\UPM\TFM\QVocoder\og_input_wavs'
output_directory = r'D:\UPM\TFM\QVocoder\og_output_wavs'


# Llama a la función para cambiar la frecuencia de muestreo
resample_audio(input_directory, output_directory, target_sr=22050)
