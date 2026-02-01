import subprocess

def run(cmd):
    print("[DEBUG] tshark command:")
    print(" ".join(cmd))
    subprocess.run(["tshark", "-v"])
