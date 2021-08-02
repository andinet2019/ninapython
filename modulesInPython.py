from pathlib import Path
# /usr/local/bin
path=Path()
for file in path.glob('*.py'):
    print(file)