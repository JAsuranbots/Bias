import asyncio
import os
import subprocess
import sys
import multiprocessing

def run_file1():
   os.system("python bot.py")
    # code to run file1

def run_file2():
   os.system("python server.py")
    # code to run file2

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=run_file1)
    p2 = multiprocessing.Process(target=run_file2)
    p1.start()
    p2.start()