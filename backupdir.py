import os
import shutil
from datetime import datetime

def backup_directory(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_dir = os.path.join(backup_dir, f"backup_{timestamp}")

    try:
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)
        print(f"Backup successful! Files copied to {dest_dir}")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    # Specify the source directory and backup directory
    source_dir = "/path/to/source"   # Replace with the directory you want to backup
    backup_dir = "/path/to/backup"   # Replace with the directory where backups should be stored
    
    backup_directory(source_dir, backup_dir)
