import subprocess
import os

# watchToMove.pyの絶対パス
script_path = os.path.join(os.path.dirname(__file__), "watchToMove.py")

# バックグラウンドで起動（ログはwatchToMove.logに保存）
subprocess.Popen(
    ["python", script_path],
    stdout=open("watchToMove.log", "a"),
    stderr=subprocess.STDOUT
)

print("watchToMove.py started in background.")

script_path = os.path.join(os.path.dirname(__file__), "watchAndPushGithub.py")

# バックグラウンドで起動（ログはwatchToMove.logに保存）
subprocess.Popen(
    ["python", script_path],
    stdout=open("watchAndPushGithub.log", "a"),
    stderr=subprocess.STDOUT
)
print("watchAndPushGithub.py started in background.")
