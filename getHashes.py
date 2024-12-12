#!/bin/python3

import hashlib
import argparse
import os
import glob

def generate_hashes(sample_bytes: bytes) -> dict:
    """
    Returns a dictionary with the MD5, SHA1, SHA256, SHA384 & SHA512 Hashes for a given Malware Sample.
    """
    return {
        "MD5": hashlib.md5(sample_bytes).hexdigest(),
        "SHA1": hashlib.sha1(sample_bytes).hexdigest(),
        "SHA256": hashlib.sha256(sample_bytes).hexdigest(),
        "SHA384": hashlib.sha384(sample_bytes).hexdigest(),
        "SHA512": hashlib.sha512(sample_bytes).hexdigest()
        }


def print_output(file: str, hashes: dict) -> str:
    return f"Getting Hashes for the File '{file}':\n\tMD5: {generated_hashes["MD5"]}\n\tSSHA1: {generated_hashes["SHA1"]}\n\tSHA256: {generated_hashes["SHA256"]}\n\tSHA384: {generated_hashes["SHA384"]}\n\tSHA512: {generated_hashes["SHA512"]}"


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Finds multiple Hashes of a File or Files.')
    parser.add_argument('-v', '--verbose', metavar='<on/off>', default='off', help='sets the output to be verbose (default = off).')
    parser.add_argument('-f', '--file', metavar='</path/to/file>', help='input the target file.' )
    parser.add_argument('-l', '--list', metavar='</path/to/list>', help='input the target file list.' )
    parser.add_argument('-d', '--directory', metavar='</path/to/directory>', help='input the targets directory.')
    parser.add_argument('-o', '--output', metavar='</output_name>' ,help='set the output file.')
    args = parser.parse_args()


    if args.file:
        target_file = args.file
        with open(target_file, 'rb') as f:
            binary_data = f.read()
            generated_hashes = generate_hashes(binary_data)
            output = print_output(target_file, binary_data)
            if args.output and args.verbose == 'off':
                with open(args.output+".file_hash", "a") as out:
                    out.write(output)
                    out.write("\n")
            elif not args.output and args.verbose == 'on':
                print(output)
            else:
                print(output)
    elif args.list:
        my_listed_files: str=args.list
        path = os.path.dirname(my_listed_files)
        with open(my_listed_files) as f:
            my_files = f.readlines()
            res = []
            for file in my_files:
                res.append(file.replace("\n",""))
            for item in res:
                with open(path+f'/{item}', 'rb') as file:
                    binary_data= file.read()
                    my_sample= binary_data
                    generated_hashes = generate_hashes(my_sample)
                    output = print_output(item, my_sample)
                    if args.output and args.verbose == 'off':
                        with open(args.output+".list_hashes", "a") as out:
                            out.write(output)
                            out.write("\n")
                    elif not args.output and args.verbose == 'on':
                        print(output)
                    else:
                        print(output)
    elif args.directory:
        my_listed_files = glob.glob(args.directory+"/*")
        for file in my_listed_files:
            with open(file, 'rb') as file:
                binary_data= file.read()
                my_sample= binary_data
                generated_hashes = generate_hashes(my_sample)
                output = print_output(file, my_sample)
                if args.output and args.verbose == 'off':
                    with open(args.output+".files_hashes", "a") as out:
                        out.write(output)
                        out.write("\n")
                elif not args.output and args.verbose == 'on':
                    print(output)
                else:
                    print(output)
    else:
        print("Instructions: ./getHashes.py --help\n\n\tExample: ./getHashes.py -f ./path/to/file.malz -o output")
