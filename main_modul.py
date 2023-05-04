from filename_or_extension import select_file_name
from files_work import find_files
from mp3_converter import convert_mp4_to_mp3


def work_with_file(dir_path, extension, final_extension):
    files_list = find_files(dir_path, extension)  # files list
    for file in files_list:
        convert_mp4_to_mp3(f'{dir_path}/{file}', f'{dir_path}/{select_file_name(file)}.{final_extension}')


if __name__ == '__main__':
    work_with_file('/Volumes/big4photo/Movies/shum', 'mp4', 'mp3')
