import subprocess

def run_python_script(script_path):
    try:
        # Use subprocess to run the Python script
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occurred during script execution
        print(f"An error occurred while running {script_path}: {e}")
