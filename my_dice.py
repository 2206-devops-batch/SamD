#rev3
import datetime
import csv

#generic function for loop
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

# displaying the contents of the CSV file
def get_row_from_file(filename, polyhedral_count):
    try:
        with open(filename, mode ='r', newline='') as csvfile:   
            sumreader = csv.reader(csvfile, delimiter=",")   #, quotechar="|"
            for x in sumreader:
                row = x
        return row
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
    
    polyhedral_count=6
    filename='DiceDATA.csv'

    print(f"\t loaded:  {get_row_from_file(filename, polyhedral_count)}")

    #build the row to be written to the file
    result_list=get_set(polyhedral_count)
    file_data_row=[str(datetime.datetime.now())]
    file_data_row.append(str(polyhedral_count))
    old_row=get_row_from_file(filename, polyhedral_count)

    new_row=old_row[2:]
    new_int_row=list(map(int, new_row))   #cast int to list so it can be written

    file_data_row.extend(sort_set(polyhedral_count, result_list, new_int_row))

    write_to_file(filename, file_data_row) 

    display_data(polyhedral_count, file_data_row)
    
main()