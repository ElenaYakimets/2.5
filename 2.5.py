import os
import subprocess


def all_list():
    source_dir = 'Source'
    os.chdir(source_dir)
    files_list = os.listdir(".")
    return files_list

def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

if __name__ == "__main__":
    files_list = all_list()
    print('Идет обработка...')
    source_dir = 'Source'
    result_dir = 'Result'
    ensure_dir(result_dir)
    os.chdir(os.path.dirname(os.path.abspath(r'/Users/elenayakimets/PycharmProjects/2.5')))
    for i in files_list:
        input_path = os.path.join(source_dir, i)
        output_path = os.path.join(result_dir, i)
        command = 'convert.exe ' + input_path + ' -resize 200 ' + output_path
        subprocess.call(command)
    print('Готово')