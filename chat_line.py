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
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len (m) 
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len (m) 
	print ('Allen：說了', allen_word_count,'個字, 傳了', allen_sticker_count, '張貼圖, 傳了', allen_image_count, '張圖片')
	print ('Viki：說了',viki_word_count, '個字, 傳了', viki_sticker_count, '張貼圖, 傳了', viki_image_count, '張圖片')
		# print (s)


# 寫入檔案
def write_file (filename, lines):
	with open (filename, 'w') as f:
		for line in lines:
			f.write (line + '\n')


# main function
def main():
	lines = read_file('Line-Viki.txt')
	lines = convert (lines)
	# write_file ('output', lines)

main() # 程式執行點