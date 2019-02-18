import csv #https://docs.python.org/2/library/csv.html
import timeit #https://docs.python.org/2/library/timeit.html

#Measuring execution time
""" s=time=timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print('\nExecution time')
print('----------------')
print (s)
print('\n') """

person_list = {} #creates persons_list

def addItem(header, data): #associate the header (first line in a csv file) with the correspondent data
    person_id='' #creates person_id
    person_data = {} #creates person_data

    #for the web auth data 
    if ('id' in header) : #check if there is an id in header 
        id_position_in_arr = header.index('id') #add a new person if there is not
        person_id = data[id_position_in_arr] #catch the item by  position the in the array 

        if person_list.get(person_id) is None:  #if person id is null (there is not a person_id)
            person_list[person_id] = person_data #catch person_id from the person_data
        else :
            person_data = person_list[person_id] #else person_data receives the person_id in person_list
    
    elif ('employeeNumber' in header) :  #then we do the same for the employees system
        id_position_in_arr = header.index('employeeNumber') 
        person_id = data[id_position_in_arr] 
        
        if person_list.get(person_id) is None:
            person_list[person_id] = person_data 
        else : 
            person_data = person_list[person_id] 

    if person_data.get('status') is None : person_data['status'] = ''

    for prop in header:
        #adding the propertys in the object
        if prop == 'employeeNumber' or prop == 'id' : #employeeNumber is equivalent to id
            person_data['InternalId'] = data[header.index(prop)]
            person_data[prop] = data[header.index(prop)]
        elif prop == 'name' or prop == 'cn' : #name is equivalent to cn
            person_data['Name'] = data[header.index(prop)]
        elif prop == 'demission_date' :
            person_data['DemissionDate'] = data[header.index(prop)]
        #if the department in the web auth csv file is different from the department in employees system then print what changes
        elif prop == 'department' and person_data.get('department') is not None and person_data.get('department') != data[header.index(prop)] :
            person_data['status'] = person_data['status'] + ' Changed department, was '+person_data.get('department')+', now it is '+ data[header.index(prop)] +';'
        #if the position in the web auth csv file is different from the position in employees system then print what changes
        elif prop == 'position' and person_data.get('position') is not None and person_data.get('position') != data[header.index(prop)] :
            person_data['status'] = person_data['status'] + ' Changed position, was '+person_data.get('position')+', now it is '+ data[header.index(prop)] +';'
        else :            
            person_data[prop] = data[header.index(prop)]    
    return

#printing the report
def printList(): 
    print('\nWoolamaloo Synchronization Report')
    print('---------------------------------------------------------------------------------------------')
    print(' ID   Name              Status')
    print('----- ----------------- ---------------------------------------------------------------------\n')

    for person in person_list.values():
        #if a person was a EmployeeNumber but has not id then its considered new
        if (person.get('id') is None and person.get('employeeNumber') is not None):
            person['status'] = person['status'] + 'was recently addmited' #+ person['AdmissionDate']
        #if a person was id but has not an EmployeeNumber then its considered a demission
        if (person.get('id') is not None and person.get('employeeNumber') is None): 
            person['status'] = person['status'] + 'was dismissed on ' + person['DemissionDate']
        #prints the id, name and what changed in person status
        print(person.get('InternalId') + '  ' + person.get('Name')+ '  ' + person.get('status'))

#open & read the CSV files, return the list of employees with its data
def readCSVFile( file ) :
    with open( file , newline='') as csvfile:
        lista = csv.reader( csvfile , delimiter=',' , quotechar=' ')
        c=0
        list=[]
        for row in lista:
            list.insert(c,row)
            c = c+1
        return list 

def main() : 
    list_01 = readCSVFile('data_set_1.csv'); #calls readCSVFile for the employees system file
    list_02 = readCSVFile('data_set_2.csv'); #calls readCSVFile for the web auth file
    
    cnt = 0 #start a counter to keep the header 
    header = [] 

    for item in list_01:
        if cnt == 0 :
            header = item
        else : 
            addItem(header,item)
        cnt = 1+cnt

    header = [] 
    cnt = 0
    for item in list_02:
        if cnt == 0 :
            header = item
        else : 
            addItem(header,item)
        cnt = 1+cnt  
    printList() #calls printList function
main()