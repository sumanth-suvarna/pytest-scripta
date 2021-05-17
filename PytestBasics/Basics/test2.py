class Example:
    MY_CLASS_VAR = "Class Var"
    Var1 = "Variable1"
    Var2 = "Variable2"
    Var3 = "Variable3"

    def get_variables(self):
        myvar1 = self.Var1
        myvar2 = Example.Var2
        self.Var1 = "Variable1_Edited"
        print(myvar1)
        print(myvar2)
        print(self.Var1)

ex = Example()
print(ex.MY_CLASS_VAR)
print(Example.MY_CLASS_VAR)
ex.MY_CLASS_VAR = "Edited Instance Var"
Example.MY_CLASS_VAR = "Edited Class Var"
print(ex.MY_CLASS_VAR)
print(Example.MY_CLASS_VAR)

ex2 = Example()
print(ex2.MY_CLASS_VAR)
print(Example.MY_CLASS_VAR)


ex2.MY_CLASS_VAR = "Edited Instance Var2"
print(ex.MY_CLASS_VAR)
print(ex2.MY_CLASS_VAR)


ex2.get_variables()
ex2.get_variables()
ex.get_variables()
print(Example.Var1)