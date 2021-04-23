from parameterized import parameterized

@parameterized.expand(['5','10'])
def cube(a):
    nunber = int(a)
    cube = nunber*nunber
    print(f"Binh phuong cua {nunber} la {cube}")
cube()