
f_4 = open('final.txt', 'w')

f_1 = open ('2.txt')
f_4.write('2.txt \n')
f_4.write(f'{str(len(f_1.readlines()))}\n')
f_1.close()

f_1 = open ('2.txt')
f_4.write(f'{f_1.read()}\n')
f_1.close()

f_2 = open('1.txt')
f_4.write('1.txt \n')
f_4.write(f'{str(len(f_2.readlines()))} \n')
f_2.close()

f_2 = open('1.txt')
f_4.write(f'{f_2.read()} \n')
f_2.close()

f_3 = open('3.txt')
f_4.write('3.txt \n')
f_4.write(f'{str(len(f_3.readlines()))}\n')
f_3.close()

f_3 = open('3.txt')
f_4.write(f'{f_3.read()} \n')
f_3.close()


f_4.close()