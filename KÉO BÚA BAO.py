import random
import time		
print ('GAME KÉO BÚA BAO ĐẤU VỚI MÁY')
print ('*' * 28)
print ('CÁCH CHƠI \nKÉO := 1\nBÚA := 2\nBAO := 3')
print ('-' * 17)
while True:
	opt = ["KÉO" ,"BÚA" , "BAO"]
	PC = random.randint(1,3)
	while True:
		PL = int(input('BẠN CHỌN := '))
		if PL > 3:
			print ("MỜI BẠN NHẬP LẠI")
		if PL <= 3:
			break	
	print ('-' * 17)
	if PL== 1:
		PL = opt[0]
	elif PL == 2:
		PL = opt[1]
	else:
		PL = opt[2]

	if PC == 1:
		PC = opt[0]
	elif PC == 2:
		PC = opt[1]
	else:
		PC = opt[2]
	print("KẾT QUẢ TRÒ CHƠI")
	print("BẠN CHỌN := ", PL)
	time.sleep (1)
	print("MÁY CHỌN := ", PC)
	print ('-' * 17)	
	print("==>")
	time.sleep (1)
	if PL == PC:
		print ("BẠN ĐÃ HÒA")
	else:
		if PL == opt[0]: 
			if PC == opt[1]:
				print ("BẠN ĐÃ THUA")
			if PC == opt[2]:
				print ("BẠN ĐÃ THẮNG")
		if PL == opt[1]:
			if PC == opt[0]:
				print ("BẠN ĐÃ THẮNG")
			if PC == opt[2]:			
				print ("BẠN ĐÃ THUA")
		if PL == opt[2]:
			if PC == opt[1]: 
				print ("BẠN ĐÃ THUA")
			if PC == opt[0]:
				print ("BẠN ĐÃ THẮNG")
	print ("*" * 30)
	time.sleep (1)
	while True:				
		b = int(input("TIẾP TỤC CHƠI BẤM PHÍM 1 / KẾT THÚC BẤM PHÍM 0 := "))
		if b > 1:
			print ("MỜI BẠN NHẬP LẠI")
		if b <= 1:
			break	
	if b == 0:
 		break					