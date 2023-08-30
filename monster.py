#-1
monster_list =  [1,11,14,5,8,9] 

def monster_function(monsters):
    empty_list = []
    for monster in monsters:
        if monster < 10:
            empty_list.append(monster)
    # print(empty_list)
    return empty_list

new_monsters = monster_function(monster_list)
print(new_monsters)






# The player has two lists of weapons, each with different levels of power. The player wants to merge the two lists and sort them in order to better organize their inventory. However, the player also has limited space in their inventory and can only keep a certain number of weapons. Write a function that takes in two lists of weapon power levels, a maximum inventory size, and returns a single list with the top N weapon levels, sorted in descending order of power, utilizing slicing techniques.
# For example, if the function takes the lists [1, 2, 3, 4, 5, 6] and [3, 4, 5, 6, 7, 8, 10], and the maximum inventory size is 8, it should return [10, 8, 7, 6, 6, 5, 5, 4].
# Use the following lists and maximum inventory size:

# -2
weapons_list1 =[1, 2, 3, 4, 5, 6] 
weapons_list2 = [3, 4, 5, 6, 7, 8, 10]
inventory = 8

def weapon_fucntion(weapons_list1, weapons_list2, inventory):  #3 inputs
    
    weapons = weapons_list1 + weapons_list2
    weapons.sort()
    weapons.reverse()
    # print(weapons)
    for weapon in weapons:
        if weapon < 3:
            weapons.pop(weapon)
        elif len(weapons) > inventory:
            weapons.pop(-1)
    # print(weapons)     
    return weapons

new_inventory = weapon_fucntion(weapons_list1, weapons_list2, inventory)
print(new_inventory)