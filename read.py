
date = [] #3.建立date這空清單
count = 0 #8.預設 計數 為0
with open('reviews.txt', 'r') as f:#1.開啟檔案 把檔案當作f

	for line in f: #2.每次讀取都讀取一行(line)在f的檔案
		date.append(line) #4.把line加入 date這空清單裡面
		count = count + 1 #9.每讀一筆 我就+1 (快寫 count += 1)
		if count % 1000 == 0: #10.如果count的餘數是0 (在數學 -如果是1000的倍數就把妳印出來) (%餘數) 
			print(len(date)) #7.每讀一行就把它長度印出來
print(len(date)) #5.印出date清單的長度 有多少東西
print(date[0]) #6.index 此檔案的第一筆 (電腦第一筆都是0開始)