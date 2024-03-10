import subprocess
import time

# Set PYTHONPATH environment variable
subprocess.run('set PYTHONPATH=.', shell=True)
time.sleep(3)
# Run 'python main.py cam' in a separate process
cam_process=subprocess.Popen(['python', 'main.py', 'cam'])

# Wait for 1 second
# time.sleep(1)

# Run 'python main.py mic' in the current process
audio_process=subprocess.run(['python', 'main.py', 'mic'])

# time.sleep(1)
# cam_process.terminate()
# audio_process.terminate()

