import os
from flask import Flask, jsonify
import demucs.api

app = Flask(__name__)

# Inicializa o separador
separator = demucs.api.Separator()

@app.route('/')
def process_audio():
    # Caminho do arquivo de áudio a ser processado
    audio_file_path = './audio.wav'  # Coloque o nome do seu arquivo de áudio aqui

    # Verifica se o arquivo de áudio existe
    if not os.path.exists(audio_file_path):
        return jsonify({'message': 'Arquivo de áudio não encontrado'}), 404

    # Realiza a separação de fontes
    try:
        _, separated_sources = separator.separate_audio_file(audio_file_path)
    except Exception as e:
        return jsonify({'message': f'Erro ao processar o arquivo de áudio: {str(e)}'}), 500

    # Envia a mensagem de conclusão
    return jsonify({'message': 'Processamento concluído'}), 200

if __name__ == '__main__':
    app.run(debug=True)
