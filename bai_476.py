class Solution(object):
    def findComplement(self, num):
        #doi num sang dang nhi phan va loai bo cac so 0 thua o dau chuoi
        binary = bin(num)[2:].lstrip('0')
        #lat nguoc tung bi trong chuoi nhi phan 
        c = ''.join(['1' if bit == '0' else '0' for bit in binary])
        #chuyen chuoi nhi phan moi ve dang so nguyen va tra ve kq
        return int(c,2)