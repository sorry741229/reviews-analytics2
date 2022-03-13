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

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每筆留言平均是', sum_len/len(data))