"""This script was writen by offensive soldier to demonstrate collision attack-Broken sha-1
You can visit this website for more information and download the files
https://shattered.io/
  """
import hashlib

def hash_file(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()

file1 = 'shattered-1.pdf'
file2 = 'shattered-2.pdf'

print(f"SHA-1 Hash of {file1}: {hash_file(file1)}")
print(f"SHA-1 Hash of {file2}: {hash_file(file2)}")
