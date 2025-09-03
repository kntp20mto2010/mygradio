import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# REPO_PATH = "/notebooks/FramePack"  # resultsフォルダが含まれるGitリポジトリのパス
# RESULTS_PATH = os.path.join(REPO_PATH, "results")

REPO_PATH = "/notebooks/FramePack/results"
RESULTS_PATH = REPO_PATH

class GitAutoPushHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.png'):
            print(f"New file detected: {event.src_path}")
            # Git add, commit, push
            try:
                subprocess.run(["git", "add", event.src_path], cwd=REPO_PATH)
                subprocess.run(["git", "commit", "-m", f"Add {os.path.basename(event.src_path)}"], cwd=REPO_PATH)
                subprocess.run(["git", "push"], cwd=REPO_PATH)
                print("Pushed to GitHub!")
            except Exception as e:
                print(f"Git push failed: {e}")

if __name__ == "__main__":
    event_handler = GitAutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, RESULTS_PATH, recursive=False)
    observer.start()
    print("Watching for new files in results/ ...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()