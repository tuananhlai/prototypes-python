empty_dict = {}
cats_list = ['Henri', 'Grumpy', 'Lucy']
animals_dict = {
    'cats': cats_list,
    'octopi': empty_dict,
    'emus': empty_dict
}
life = {
    'animals': animals_dict,
    'plants': empty_dict,
    'other': empty_dict
}
print(life['animals']['cats'])