from pathlib import Path

a = Path('a.txt')
with a.open('w',encoding='utf-8') as file:
	file.write('hello')