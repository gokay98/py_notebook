import argparse

class araba():
    """class ozellikleri"""
    def  __init__(self,model = "N/A",sene = 0 ,renk= "N/A",silindir = 0):
        self.model = model
        self.sene = sene
        self.renk = renk
        self.silindir = silindir
       

    """method oluışturma kısmı"""

    def data_show(self):
        print("""Araba obje ozellikleri:\n
              Model: {}\nSene: {}\nRenk: {}\nSilindir: {}\n"""
              
              .format(self.model,self.sene,self.renk,self.silindir))
        

def main():
    argparser = argparse.ArgumentParser(
        description='Hello from the arg parser')
     
    argparser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='func',
        help='what do you need')

    argparser.add_argument(
        '-p', '--print',
        action='store_true',
        dest='helpp',
        help='what do you need')
    
    
    args = argparser.parse_args()


    if args.func:
        araba1 = araba("opel",2010,"siyah",4)

        print(araba1.data_show())
         
    if args.helpp:
    
        print( "Hello from the arg parser") 



if __name__ == "__main__":
    main()


