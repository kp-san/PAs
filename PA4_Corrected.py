#PA4 Corrected
"""
Created on Tue Apr  2 10:29:53 2024

@author: KTSanNicolas
"""

def bubbleSort(a_list):
    for passnum in range(len(a_list)-1,0,-1):
        for i in range(passnum):
            if a_list[i]>a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp

def convert_input_to_int(input_list):
    word_to_number = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
    }
    converted_list = []
    for item in input_list:
        if item.isdigit():
            converted_list.append(int(item))
        else:
            try:
                num = int(item)
                if 1 <= num <= 10:
                    converted_list.append(num)
                else:
                    print(f"Warning: {item} is not between 1 and 10. Discarding it.")
            except ValueError:
                if item.lower() in word_to_number:
                    converted_list.append(word_to_number[item.lower()])
                else:
                    print(f"Warning: {item} cannot be converted to an integer. Discarding it.")
    return converted_list

def main():
    user_input = input("Enter a list of numbers (separated by spaces): ").split()
    integer_list = convert_input_to_int(user_input)
    bubbleSort(integer_list)
    print("Sorted list:", integer_list)
    print("Max in sorted list:", max(integer_list))
    print("Min in sorted list:", min(integer_list))

main()