import subprocess

def run_main():
    program_path = "./main.py"  
    #subprocess.run(["start", "cmd", "/k", "python", program_path], shell=True)
    subprocess.Popen(["start", "cmd", "/k", "python", program_path], shell=True)

run_main()