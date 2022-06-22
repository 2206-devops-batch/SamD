#rev4
import datetime
import csv
import argparse

# usage: my_dice.py [-h] [--sum] N [N ...]
parser = argparse.ArgumentParser()
parser.add_argument(dest="argument1", type=int, nargs="?", help="enter the result of a dice roll to see what numbers come up the most")

'''class Dice():
    def __init__(self, polyhedral_count = 6):
'''
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
        print(f"loaded file...")
        return file_aaray

    except FileNotFoundError:     #if no file create and empty one
        print("no file loaded...")
        with open(filename, 'w', newline='') as csvfile:
            empty_string = [str(datetime.datetime.now())]
            empty_string.append(polyhedral_count)
            for i in my_range(1, polyhedral_count, 1):
                empty_string.append('0')
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(empty_string)
        return empty_string
            
# writing to csv file
def write_to_file(filename, data_row):

    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(data_row)

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

def main():
 
    #default
    polyhedral_count=6

    # Parse command line
    args = parser.parse_args()
    if args.argument1:     #if there is an argument set
        polyhedral_count = args.argument1
    
    filename='DiceDATA.csv'

    data_row=get_file_array(filename, polyhedral_count)
    if data_row[0][1] == str(polyhedral_count):
        print(f"loaded:  {data_row[0]}")
        working_data_row=list(map(int, data_row[0][2:]))
    else:
        working_data_row=[]
        for i in range(polyhedral_count):
            working_data_row.append(0)
        print(f"profile: {working_data_row}")

    #build the row to be written to the file
    result_list=get_set(polyhedral_count)

    file_data_row=[]
    file_data_row.extend(sort_set(polyhedral_count, result_list, working_data_row))

    if data_row[0][1] == str(polyhedral_count):
        lema=str(data_row[0][1])
        delta=str(data_row[0][0])
        file_data_row.insert(0, lema)
        file_data_row.insert(0, delta)
        data_row[0]=file_data_row
    else:
        file_data_row.insert(0, str(polyhedral_count))
        file_data_row.insert(0, str(datetime.datetime.now()))
        data_row.insert(0, file_data_row)

    display_data(polyhedral_count, file_data_row)

    write_to_file(filename, data_row) 
    
main()