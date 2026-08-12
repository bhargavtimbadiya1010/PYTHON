'''Write a program to illustrate variable scope 
using local global and nonlocal variables. '''

v_global = 10  

def non():
    v_nonlocal = 20      

    def loc():
         v_local = 30
         nonlocal v_nonlocal
         v_nonlocal = 50
         print("Local variable: ", v_local)
         print("Nonlocal variable: ", v_nonlocal)
         print("Global variable inside function: ", v_global)
    loc()

    print("Nonlocal variable after", v_nonlocal)

non()

print("Global variable after function: ", v_global)
