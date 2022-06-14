'''
rev0.1
'''

# usage: my_dice.py [-h] [--sum] N [N ...]
'''class Dice():
    def __init__(self, polyhedral_count = 6):
        self.r = polyhedral_count = 6
        self.my_list = [] 
    #polyhedral_count = 6
   # my_list = []'''
def get_set(polyhedral_count, my_list):
    
    while True:
        value = input("Enter a number: ")
        #end on done
        #add options to remove last input
        if value == "done" :
            break
        try:
            value = int(value)
            if value > polyhedral_count:
                print(f"{value} is greater than {polyhedral_count}")
                continue
            elif value <= 0:
                print("cannot be less than zero")
            else:
                my_list.append(value)

        except:
            print("Invalid input:")
            continue
    return my_list

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def sort_set(polyhedral_count, my_list):
    for i in my_range(1, polyhedral_count, 1):
            print(f"{i}: {my_list.count(i)}")

def main():
    '''dice1=Dice()
    dice1.get_set()'''
    #sort_set(get_set(6)
    polyhedral_count=7
    my_list=[]
    new_list = get_set(polyhedral_count, my_list)
    #print(new_list)
    sort_set(polyhedral_count, my_list)
main()