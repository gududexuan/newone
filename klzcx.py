number = input("请给我一个数字：")
number=int(number)
kfc=0
niupai=[]
while number !=1:
    number_a=number % 2
    if number_a == 0:
        kfc=kfc+1
        number=number/2
        niupai.append(number)
    else:
        kfc=kfc+1
        number=(number*3)+1
        niupai.append(number)
print("程序一共被执行了："+str(kfc) +"次")
print("运行中生成数列如下：")
print(niupai)