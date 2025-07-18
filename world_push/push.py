import os, shutil, subprocess
from datetime import datetime

# === CHANGE THIS: Minecraft world folder path
world_folder = r"C:\Users\YourName\AppData\Roaming\.minecraft\saves\MyWorld"

# ===  CHANGE THIS: Your local GitHub repo path
repo_path = r"C:\Users\YourName\git\my-backup-repo"

# === Find next folder name: MyWorld1, MyWorld2, etc.
i = 1
while True:
    backup_name = f"MyWorld{i}"
    backup_path = os.path.join(repo_path, backup_name)
    if not os.path.exists(backup_path):
        break
    i += 1

# ===  Copy the world
shutil.copytree(world_folder, backup_path)
print(f"Copied world to: {backup_path}")

# ===  Git add, commit, push
subprocess.run("git add .", cwd=repo_path, shell=True)
subprocess.run(f'git commit -m "Backup {backup_name} - {datetime.now()}"', cwd=repo_path, shell=True)
subprocess.run("git push origin main", cwd=repo_path, shell=True)
