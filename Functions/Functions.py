def find_total(expenses):

    #Important to have documentation for functions in big projects
    '''
    :param expenses: Inputs a list that contains expense numbers
    :return: The sum of all the expenses present in the list
    '''

    total = 0
    for expense in expenses:
        total += expense

    return total



expenses_steph = [30,45,70,90]
expenses_kyrie = [40,23,10,85]


print(f"Total expenses for Kyrie: {find_total(expenses_kyrie)}")
print(f"Total expenses for Steph: {find_total(expenses_steph)}")


