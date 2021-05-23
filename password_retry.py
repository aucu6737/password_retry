password = 'a123456'
x = 1
while x <= 3:
	if input('請輸入密碼: ') == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有', 3-x, '次機會')
		x = x + 1
