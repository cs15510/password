password = "a123456"
fail_count = 0

while fail_count < 3:
	input_password = input("請輸入密碼(您有3次機會):")
	if input_password == password:
		print("登入成功")
		break
	else:
		fail_count += 1
		if fail_count < 3:
			print("密碼錯誤, 還有", 3-fail_count, "次機會")
		else:
			print("密碼錯誤, 您沒有機會了")