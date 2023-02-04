lines =[]

with open ('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())  # 去除換行符號

for line in lines:
	s = line.split(' ')  # 以'空白格'為基準進行分割
	time = s[0][:5]  # 小索引中，前五個索引皆為「時間」的值
	name = s[0][5:]  # 小索引中，第五個值開始為「名字」
	print (name)
 
