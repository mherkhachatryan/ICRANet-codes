import glob
import shutil
import subprocess
import argparse


def get_result_files(base_dir, extension):
    return glob.iglob("{}/**/*.{}".format(base_dir, extension))


def copy_file(working_dir, destination, extension):
    filenames = list(get_result_files(working_dir, extension))
    for file in filenames:
         shutil.copy(file, destination)



parser =argparse.ArgumentParser()
parser.add_argument("-b", "--base_dir", help = "Directory to check for file")
parser.add_argument("-e", "--extension", default = "results", help="Extension of the file to copy")
parser.add_argument("-d", "--destination", help="Directory to copy files")

args = parser.parse_args()

copy_file(working_dir=args.base_dir, destination=args.destination, extension=args.extension)

