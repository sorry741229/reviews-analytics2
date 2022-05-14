#留言分析程式
data = []
count= 0 

with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0 :
			print(len(data))
print('檔案讀取完畢，共有', len(data),'筆資料')
print(data[0])

sum_len = 0
for d in data:
	 sum_len = sum_len + len(d)
print('每筆留言平均是', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('共有', len(good), '筆留言提到Good')



#文字記數
wc = {} #word_ count
print('讀取中請稍後...')
for d in data:
	words = d.split(' ')
	for word in words:    
		if word in wc:  
			wc[word] +=1
		else:
			wc[word] = 1 #新增新的字加入wc字典


for word in wc:
	if wc[word] > 100:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		print('感謝使用本查詢系統')
		break
	elif word in wc:
		print(word,'出現過的次數為' ,wc[word])
	
	else:
		print(word, '沒有出現過' )
		continue



