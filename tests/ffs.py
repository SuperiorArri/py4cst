from py4cst import FFS

parser = FFS.Parser()
with open('C:/Users/Samuel/Documents/MATLAB/FFS/data/Farfield Source_A.ffs') as file:
    parser.parse_string(file.read())
farfields = parser.get_farfields()
ff1 = farfields[0]
prod,_,_ = FFS.Farfield.get_inner_product(ff1, ff1)
print(prod)