class Person():
    __name: str= None
    __family: str= None
    
    def __init__(self):
        pass

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,x):
        self.__name=x
        
    
    @property
    def family(self):
        return self.__family
    
    @family.setter
    def family(self,y):
        self.__family=y
        
class Contact():
    
    __contact = {'PhoneNumber': None, 'Person': Person} 
    __records=''
    __data={}
    def __init__(self):
        pass
    
    def add(self,data):
        with open('db.txt','a') as f:
            f.write(data+'\n')
     
            
            
    def show_all(self):
       
        self.__records=''
        with open('db.txt','r') as f:
            for line in f:
                self.__records+= line
        return self.__records
    
    def delete(self):
        pass
    
    def get_contact(self,no: str):
        self.__data= {}
        with open("db.txt") as f:
            for line in f:
                (key, val) = line.split(':')
                self.__data[key] = val.replace('\n','')
        return self.__data[no]
                
    def dail(self,no):
        print("Contact Name : "+self.get_contact(no))
        
        print("               is Dialing right now ...")
