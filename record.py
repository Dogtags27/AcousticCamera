import subprocess
import time

# Set PYTHONPATH environment variable
subprocess.run('set PYTHONPATH=.', shell=True)

# Run 'python main.py cam' in a separate process
subprocess.Popen(['python', 'main.py', 'cam'])

# Wait for 1 second
time.sleep(10)

# Run 'python main.py mic' in the current process
subprocess.run(['python', 'main.py', 'mic'])