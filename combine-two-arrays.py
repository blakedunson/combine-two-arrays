#!/usr/bin/python
import sys

def main():
    try:
        # Collect the input
        input = ' '.join(sys.argv[1:])

        # Parse input into two strings that look like lists
        input = input.replace(" ", "")
        input = input[1:-1]
        input = input.split("][")
        if len(input) != 2:
            raise Exception("")

        # Convert the strings into lists of ints
        list_one = parse_list(input[0])
        list_two = parse_list(input[1])

        # Combine the two lists into a single sorted list
        combined_list = combine_lists(list_one, list_two)

        # Output the result
        print(combined_list)

    except:
        print("Input is invalid!")
        print("Example Command: docker run combinetwoarrays [1, 2, 7, 9] [3, 6, 8]")

def parse_list(list_to_parse):
    # Convert from string representation to a list of ints
    parsed_list = list_to_parse.split(",")
    parsed_list = [int(i) for i in parsed_list]
    
    # Check to ensure list is sorted
    is_sorted = False
    if(all(parsed_list[i] <= parsed_list[i + 1] for i in range(len(parsed_list)-1))):
        is_sorted = True
    
    if not is_sorted:
        raise Exception("")

    return parsed_list

def combine_lists(list_one, list_two):
    combined_list = []
    n1 = len(list_one)
    n2 = len(list_two)
    i1 = 0
    i2 = 0

    # Iterate through the lists picking the lowest int available until one runs out
    while i1 < n1 and i2 < n2:
        if list_one[i1] < list_two[i2]:
            combined_list.append(list_one[i1])
            i1 += 1
        else:
            combined_list.append(list_two[i2])
            i2 += 1
            
    # Fill out the rest of the first list if it has leftover values
    while i1 < n1:
        combined_list.append(list_one[i1])
        i1 += 1
    
    # Fill out the rest of the second list if it has leftover values
    while i2 < n2:
        combined_list.append(list_two[i2])
        i2 += 1

    return combined_list

if __name__ == "__main__":
    main()

