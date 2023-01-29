# python chat.py

# 讀取檔案
def read_file (filename):
	lines = []
	with open (filename, 'r', encoding="utf-8-sig") as f:
		for line in f:
			lines.append (line.strip())
	return lines

# 格式傳換
def convert (lines):
	new = []
	person = None  # 假設若第一行不是人名
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:  # 若person有值才進入迴圈
			new.append (person + ':' +line)
	return new

# 寫入檔案
def write_file (filename, lines):
	with open (filename, 'w') as f:
		for line in lines:
			f.write (line + '\n')

# main function
def main():
	lines = read_file('input.txt')
	lines = convert (lines)
	write_file ('output', lines)

main() # 程式執行點