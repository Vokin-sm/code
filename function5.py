def my_function(n,k):
    total_sum=0
    print ("коэффициент n равен "+str(n))
    print ("коэффициент k равен "+str(k))
    if n>20:
        return "введите коэффициент n меньше, либо равный 20"
    if n<=20:
        for i in range(1,n):
            if i%2==0:
                total_sum=total_sum+i**k
        return "сумма четных чисел от 1  до n в степени k равна " + str(total_sum)        
a=my_function(16,2)
print(a)
                
