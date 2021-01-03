
data = [] #3.建立data這空清單
count = 0 #8.預設 計數 為0
with open('reviews.txt', 'r') as f:#1.開啟檔案 把檔案當作f
	for line in f: #2.每次讀取都讀取一行(line)在f的檔案
		data.append(line) #4.把line加入 data這空清單裡面
		count = count + 1 #9.每讀一筆 我就+1 (快寫 count += 1)
		if count % 1000 == 0: #10.如果count的餘數是0 (在數學 -如果是1000的倍數就把妳印出來) (%餘數) 
			print(len(data)) #7.每讀一行就把它長度印出來
print('檔案讀取完了,總共有',len(data), '筆資料' ) #11

sum_len = 0 #14.sum_len 加總長度
for d in data: #12.一筆一筆讀 每一筆資料命名d 把date清單100萬筆的資料 每一筆字串都叫d
	len(d) #13.字串求長度 求d的長度 每一筆d的長度
	sum_len = sum_len + len(d) #15.每一筆長度+目前的總數加再一起，存回目前的總數
print('留言的平均長度', sum_len / len(data)) #16.平均=總長度/date的長度(100萬)

