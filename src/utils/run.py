import argparse
import os

def main():

    verbosity = 5
    filename = 'theorem00_13'
    current_proof = ''
    # current_proof = 'ws,wr,wp,w2,w2'

    if current_proof != '':
        os.system(f"python3 mmverify.py {filename} --logfile {filename}-{verbosity}.log -v {verbosity} -p {current_proof}")
    
    else:
        os.system(f"python3 mmverify_zero.py {filename} --logfile {filename}-{verbosity}.log -v {verbosity}")
    
    # os.system(f"python mmverify.py < {filename}.mm")
    # os.system(f"python mmverify.py < {filename}.mm 2> {filename}.log")

    
if __name__ == "__main__":
    main()
   
