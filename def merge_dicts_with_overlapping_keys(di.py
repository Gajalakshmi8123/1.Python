def merge_dicts_with_overlapping_keys(dicts):
    
    my_dict={}

    for i in dicts:
        my_dict.update(i)


    return my_dict
    


print(merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]))
print(merge_dicts_with_overlapping_keys([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))