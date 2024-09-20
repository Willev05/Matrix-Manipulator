class Matrix:
    def verify(matrixList):
        #Check to see if it is a list to begin with
        if not isinstance(matrixList, list):
            return []
        previousRowElementAmount = -2

        for row in matrixList:
            #Verify to see if each row is a list
            if not isinstance(row, list):
                return []
            
            #Verify to see if eacch element of the matrix is an int or float
            for rowElement in row:
                if not (isinstance(rowElement, int) or isinstance(rowElement, float)):
                    return []
                
            #Makes sure each rows are the same length
            currentRowElementAmount = len(row)
            if (currentRowElementAmount != previousRowElementAmount and previousRowElementAmount != -2):
                return []
        
        return matrixList
    
    
    def Matrix(self, matrixElements):
        self.elements = verify(matrixElements)
        self.columns = len(self.elements)
        self.rows = len(self.elements[0])
    