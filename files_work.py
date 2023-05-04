import os


def find_files(dir_path, extension):  # find all files with extension in directory
    return [f for f in os.listdir(dir_path) if f.endswith(extension)]


if __name__ == '__main__':
    print(find_files('/Volumes/big4photo/Movies/АГАТА КРИСТИ', 'mp4'))
