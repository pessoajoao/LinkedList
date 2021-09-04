class No:
    def __init__(self, carga: object = None, prox:'No' = None):
        self.carga = carga
        self.prox = prox
    
    def __str__(self):
        return str(self.carga)

class ArrayList:
    def __init__(self, header = None, tail = None):
        self.header = header
        self.tail   = tail
    
    def addInFirstPosition(self, valor):
        newNo = No(valor)
        if(self.header is None):
            self.header = self.tail = newNo
        
        else:
            newNo.prox = self.header
            self.header= newNo

    def add(self, valor):
        newNo = No(valor)
        if(self.header is None):
            self.header = self.tail = newNo
        
        else:
            self.tail.prox = newNo
            self.tail = newNo

    def printList(self):
        if(self.header is None):
            print("ArrayList is none.")
            return

        no: 'No' = self.header
        while no is not None:
            print(str(no.carga) + " ")
            no = no.prox
    
    def removeTheFirstPosition(self):
        if(self.header is None):
            print("ArrayList is none.")
            return

        if(self.header == self.tail):
            self.header = self.tail = None

        else:
            self.header = self.header.prox

    def remove(self):
        if(self.header is None):
            print("ArrayList is none.")
            return
        
        if(self.header == self.tail):
            self.header = self.tail = None
        
        else:
            no: 'No' = self.header
            while no.prox is not self.tail:
                no = no.prox
            
            self.tail = no
            no.prox = None
