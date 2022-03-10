"""
Application : Webp Converter
File name   : webp_convert.py
Authors     : Jacob Summerville
Description : This file converts image files to webp using Google's
              cwebp conversion tool
"""

import argparse
import os
import shutil
import subprocess

def get_arguments():
    """ Read in command lines arguments """
    parser = argparse.ArgumentParser(description='This program converts image files to webp')
    parser.add_argument('-d', '--dir',  help='Directory to convert')
    parser.add_argument('-f', '--file', help='File to convert')
    return parser.parse_args()

def convert_webp(filename, new_file, verbose=False):
    """ Perform the webp file conversion """
    output = subprocess.run(['cwebp', '-q', '80', filename, '-o', new_file + '.webp'], capture_output=True)
    
    if verbose and output.returncode == 0:
        print(new_file + '.webp created')
    elif verbose and output.returncode != 0:
        print('Unable to convert', filename)

    return output

def convert_dir(directory):
    """ Iterate through a directory to convert each image file """
    if os.path.isdir('webp'):
        shutil.rmtree('webp')
    os.mkdir('webp')

    converted = 0
    for file in os.listdir(directory):
        filename = os.path.join(directory, file)
        if os.path.isfile(filename):
            new_file = os.path.join('webp', file.split('.')[0])
            output = convert_webp(filename, new_file)

            if output.returncode != 0:
                print(filename, 'had an issue converting')
            else:
                converted += 1

    print(converted, 'files converted')

def main():
    """ Main python function for the webp converter """
    args = get_arguments()

    if args.dir:
        if os.path.isdir(args.dir):
            convert_dir(args.dir)
        else:
            print('Directory does not exist')
    elif args.file:
        if os.path.isfile(args.file):
            new_file = args.file.split('.')[0]
            convert_webp(args.file, new_file, True)
        else:
            print('File does not exist')
    else:
        print('Run with -d [directory] or -f [file]')

if __name__ == '__main__':
    main()