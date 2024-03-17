from pathlib import Path

path=Path()
for file in path.glob('*.py'):
    print(file)

#path=Path("Newdirectory")
#print(path.mkdir())

path=Path("Newdirectory")
print(path.exists())

