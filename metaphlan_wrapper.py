import argparse
import subprocess
import os
import sys

def check_file_exists_or_die(file_name):
    if not os.path.isfile(file_name):
        print "ERROR: file " + file_name + " does not exist: check the file name and path."
        sys.exit(1)

def run_command(command, error_message):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print error_message

def get_args():
    parser = argparse.ArgumentParser(description="Runs Metaphlan2.")
    parser.add_argument("-1", "--R1", required=True, type=str, help="R1.fastq")
    parser.add_argument("-2", "--R2", required=True, type=str, help="R2.fastq")
    parser.add_argument("-o", required=True, type=str, help="output file")
    args = parser.parse_args()
    check_file_exists_or_die(args.R1)
    check_file_exists_or_die(args.R2)
    return(args)

def run_metaphlan(R1, R2, out):
    command = ("python /home/ashwini/ash/other_softwares/metaphlan2/metaphlan2.py " + R1 + ", " + R2 +
               " --mpa_pkl " + "/home/ashwini/ash/other_softwares/metaphlan2/db_v20/mpa_v20_m200.pkl" +
               " --bowtie2db /home/ashwini/ash/other_softwares/metaphlan2/db_v20/mpa_v20_m200" +
               " --bowtie2out " + out + ".bowtie2.bz2" +
               " --nproc 5" +
               " --input_type fastq > " + out +".txt")
    run_command(command, "Cannot run MetaPhlAn2. Check input files")

def main():
    args = get_args()
    run_metaphlan(args.R1, args.R2, args.o)

if __name__=="__main__":
    main()