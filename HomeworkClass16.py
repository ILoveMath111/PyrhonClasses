import os

def shutdown(time_in_seconds):
    os.system(f"shutdown /s /t {time_in_seconds}")

