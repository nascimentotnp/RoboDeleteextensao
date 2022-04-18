import os
import time
from pathlib import Path

# Robô utilizado para exclusão de log gerados pelos schedules dos robos do coiote#
path = 'C:\\Users\\tpaula\\Documents\\exclusão\\minuto'
pathdois = 'C:\\Users\\tpaula\\Documents\\exclusão\\dia'



# for path in Path().glob("*.log"):


# Nesse trecho do códio é passado a pasta que deseja excluir o arquivo especifico#


def unlink_files(dir_path, days):
    all_files = os.listdir(dir_path)  # passado os arquivos encontrados naquela pasta
    now = time.time()  # instante em que é rodado o código
    seconds_in_a_day = 60 * 60 * 24  # tempo em segundos
    seconds_by_days = days * seconds_in_a_day  # valor passado em dias e multiplicado pelo valor setado em days dentro do def

    for file in all_files:  # um for passado dentro da all_files para encontar um arquivo que dentro do if esta especificado, podemos passar varias extensões
        file_path = os.path.join(dir_path,
                                 file) #Variavel criada para mostrar os arquivos contidos dentro da pasta especifica
        if os.stat(file_path).st_mtime < (now - seconds_by_days) and os.path.isfile(
                file_path) and '.log' in file:
            # if feito para comparar o tempo do arquivo e se ele é na data que eu quero excluir e a extensão que devemos excluir
            os.unlink(file_path)  # mostra o que deve ser excluido e executa
            print(" Arquivo deletado : ", file)


unlink_files(path, 0)
unlink_files(pathdois, 0)
