password = 'a123456'
x = 0
while x <= 3: 
	if input('請輸入密碼: ') == password: 
		print('登入成功')
		break 
	else:
		print('密碼錯誤!') 
		x = x + 1
		if x == 3:
			print('沒機會嘗試了! 要鎖帳號了! ')
			break
		else: 
			print('還有', 3 - x, '次機會')
