#CSV sorter
#This short program takes in two unsorted CSV files and outputs a single CSV document sorted by the columns (emitting the first two rows)
#Chris Spencer

from string import join

class HeaderObject: #object to incorperate column name and index placement of the header row
    column_name = ''
    column_number = 0

    def __init__(self, name, number): 
        self.column_name = name
        self.column_number = number

def sort_key(x):
    return x.column_name

def main(FILES):
    sorted_header_list = [] #header OBJECTS will go here (name and index)
    
    with open(FILES[0], 'rb') as f:
        f.readline()  
        f.readline()    
        
        raw_header = f.readline().strip().split(',') #strip takes off new line, header is 3rd row (this is for Chris, please disregard how obvious this is)
        
        for (index, name) in enumerate(raw_header): #only for headers -> establish end order for data columns
            sorted_header_list.append(HeaderObject(name, index)) 
        sorted_header_list.sort(key=sort_key) 

    with open('newfile.csv', 'wb') as w:
        output_list = []
        index_reassignment = []
        
        for obj in sorted_header_list:
            index_reassignment.append(None) #for index out of bounds issue 
            output_list.append(obj.column_name)
            
        for (index, header) in enumerate(sorted_header_list): #fix index issues (they were initially swapped)
            index_reassignment[header.column_number] = index

        w.write(join(output_list, ',')) 
        w.write('\r\n')

        for FILE in FILES:
            with open(FILE, 'rb') as r:
                r.readline()
                r.readline()
                r.readline()
                r.readline()
                for line in r:
                    sorted_line = line.strip().split(',')
                    for (count, word) in enumerate(sorted_line):
                        output_list[index_reassignment[count]] = word
                    w.write(join(output_list, ','))
                    w.write('\r\n')
                
if __name__ == '__main__':  
    main(['P311992_BCC_TEST2_0547.csv', 'P311992_BCC_TEST2_0549.csv'])

    

        
            




   
        
        
        
