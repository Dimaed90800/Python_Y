class Table:
    
    def __init__(self,rows, cols):
        self.field = [[0 for i in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols
        
    def get_value(self, row, col):
        if  row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        
 
    def set_value(self, row, col,value):
        self.field[row][col] = value
    
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols
    
    
