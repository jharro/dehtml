def imprime_impares(vector,tam):
    for i in range(tam):
        if vector[i] % 2!=0:
            print(vector[i])
        

vector=[1,2,3,4,5]
imprime_impares(vector,3)