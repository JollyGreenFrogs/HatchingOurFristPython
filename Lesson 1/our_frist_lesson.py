"""
for a_grape in a_bunch_of_grapes:

"""
a_litter_of_puppies = ['Frisky', 'Rex','Caramel','Carl','Kathryn']
number_of_puppies = len(a_litter_of_puppies)
is_this_the_last_puupy = 1
print("'What are the names of the puppies?' Asks Tilly")
print("'The names of the puppies are,")
for a_puppy in a_litter_of_puppies:
    if is_this_the_last_puupy == number_of_puppies:
        print(f"and {a_puppy}.'", end=' ')
    else:
        print(f"{a_puppy},", end=' ')
    is_this_the_last_puupy += 1
    
    
print("' answered Sarah")
