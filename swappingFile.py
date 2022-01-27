def swapFiles():
    file1 =input('enter name of file to bbe swapped')
    file2 =input('enter name of file to be swapped with')

    open(file1, 'r') as a:
        data_a = a.read()
    
    open(file2, 'r') as b:
        data_b = b.read()

        

