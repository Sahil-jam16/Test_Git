def sort_dictionary(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

# Example usage
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = sort_dictionary(my_dict)
print(sorted_dict)
