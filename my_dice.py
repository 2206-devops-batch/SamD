
#rev4
import datetime
import csv
# usage: my_dice.py [-h] [--sum] N [N ...]
'''class Dice():
    def __init__(self, polyhedral_count = 6):
        
        self.r = polyhedral_count = 6
        self.my_list = [] 
        2022-06-20 20:37:04.524579,6,9,0,0,8,8,9
        2022-06-20 20:37:05.624579,6,4,0,0,0,0,0
        2022-06-20 20:37:06.624579,6,4,0,0,0,0,0
        2022-06-20 20:37:07.624579,6,4,0,0,0,0,0
        sam,6,41,10,20,0,5,2
        test1,6,4,0,0,0,0,0
        test2,6,4,0,0,0,0,0

    #polyhedral_count = 6
   # my_list = []'''

#generic function for loop
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def get_file_array(filename, polyhedral_count):
    file_aaray=[]
    try:
        with open(filename, mode ='r', newline='') as csvfile:   
            sumreader = csv.reader(csvfile, delimiter=",")   #, quotechar="|"
            for x in sumreader:
                file_aaray.append(x)
        print(f"loaded...")
        return file_aaray[0]

    except FileNotFoundError:     #if no file create and empty one
        print("no file")
        with open(filename, 'w', newline='') as csvfile:
            empty_string = [str(datetime.datetime.now())]
            empty_string.append(polyhedral_count)
            for i in my_range(1, polyhedral_count, 1):
                empty_string.append('0')
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(empty_string)
        return empty_string

    
    

# displaying the contents of the CSV file
def get_row_from_file(filename, polyhedral_count):
    current_row=get_file_array(filename, polyhedral_count)  
    return current_row
            
# writing to csv file
def write_to_file(filename, data_row):

    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerow(data_row)

def get_set(polyhedral_count):
    my_list = []
    while True:
        value = input("Enter a number: ")
        #end on done
        #add options to remove last input
        if value == "done" :
            break
        if value == "r" or value == "re" or value == "remove":
            my_list = my_list[:-1]     #slice item -1 off the end
            continue
        if value == "save":
            profile_name = input("save as what profile name: ")
            if profile_name == "":
                profile_name = str(datetime.datetime.now())
                print(f"saved as {profile_name}")
            else:

        try:
            value = int(value)
            if value > polyhedral_count:
                print(f"{value} is greater than {polyhedral_count}")
                continue
            elif value <= 0:
                print("cannot be less than one")
            else:
                my_list.append(value)
        except:
            print("Invalid input:")
            continue
    return my_list
'''
def sort_set(polyhedral_count, my_sort_list, file_row):
    result_list = []
    for i in my_range(1, polyhedral_count, 1): 
        x = my_sort_list.count(i)
        y = file_row[i - 1]
        result_of_adding_new_count_with_old_count = x + y
        result_list.append(str(result_of_adding_new_count_with_old_count))
    return result_list

def display_data(cnt, dta):
    for n in my_range(1, cnt, 1):
        new_dta = dta[2:]   #strp date and poly count off
        print(f"{n}: {new_dta[n-1]}") 
'''
def main():
 
    polyhedral_count=6
    
    filename='DiceDATA.csv'


    rowx = get_row_from_file(filename, polyhedral_count)
    print(rowx[0])


    '''
    print(f"\t loaded:  {get_row_from_file(filename, polyhedral_count)}")

    #build the row to be written to the file
    result_list=get_set(polyhedral_count)
    file_data_row=[str(datetime.datetime.now())]
    file_data_row.append(str(polyhedral_count))
    old_row=get_row_from_file(filename, polyhedral_count)

    new_row=old_row[2:]
    new_int_row=list(map(int, new_row))

    file_data_row.extend(sort_set(polyhedral_count, result_list, new_int_row))

    write_to_file(filename, file_data_row) 

    display_data(polyhedral_count, file_data_row)
    '''

    
main()