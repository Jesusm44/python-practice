# a = {1, 2, 3}
# b = {3, 4, 5}

# c = a.union(b)
# print(f'The union of a and b {c}')

# a = {10, 20, 30}
# b = {20, 40, 50}

# c = a.intersection(b)
# print(f'The intersection of a and b {c}')

# a = {1,2,3,4}
# b = {3,4}

# c = a.difference(b)
# print(f'The difference between a and b{c}')

# a = {1,2,3,4}
# b = {3,4,5,6}

# c = a.difference(b)
# d = b.difference(a)

# print(f'The difference between a and b: {c}')
# print(f'The difference between b and a: {d}')


# a = {1,2,3}
# b = {3,4,5}

# c = a.symmetric_difference(b)
# print(f'The symmetrical difference of a and b: {c}')

# a = {1,2}
# b = {1,2,3,4}

# c = a.issubset(b)
# print(f'The set a is a subset of b: {c}')

# list_one = [1, 2, 3, 4, 5]
# list_two = [4, 5, 6, 7]

# valor_one = set(list_one)
# valor_two = set(list_two)

# valor_tree = valor_one.intersection(valor_two)
# valor_four = valor_one.union(valor_two)
# valor_five = valor_one.difference(valor_two)

# print(f'The intersection of list 1 and list 2 is: {valor_tree}')
# print(f'The union of list 1 and two is: {valor_four}')
# print(f'The difference between list 1 and list 2 is: {valor_five}')


# users_app = {"ana", "luis", "pedro"}
# users_web = {"luis", "pedro", "maria"}

# total_both_system =  users_app.intersection(users_web)
# print(f'The intersection of app users and web users is: {total_both_system}')

# total_users = users_app.union(users_web)
# print(f'The total number of app and web users is: {total_users}')

# only_users_app = users_app.difference(users_web)
# print(f'The difference between app users and web users is: {only_users_app}')

# only_users_one = users_app.symmetric_difference(users_web)
# print(f'The symmetric difference between app users and web users is: {only_users_one}')

# data = [1,2,3,2,4,1]
# duplicate_data = []
# set_data = set()

# for i in data:
#     if i in set_data:
#         duplicate_data.append(i)
#         print(f'The duplicate number is: {i}')
#     else:
#         set_data.add(i)

# print(f'The duplicate numbers are: {duplicate_data}')

# data = [5,5,6,7,7,8]
# set_data = []

# for i in data:
#     if i in set_data:
#         continue
#     else:
#         set_data.append(i)

# print(f'{set_data}')
# print(type(set_data))

# list_one = [1,2,3,4]
# list_two = [3,4,5,6]
# set_one = set()
# set_two = set()

# for i in list_one:
#     set_one.add(i)
# for i in list_two:
#     set_two.add(i)

# inter = set_one.intersection(set_two)

# print(f'The intersection of sets is: {inter}')


# users = ["Ana", "Luis", "Ana","Pedro"]
# only_user = set()
# users_duplicate = set()

# for i in users:
#     if i in only_user:
#         users_duplicate.add(i)
#     else:
#         only_user.add(i)
    
# print(f'The only user are: {only_user} ')
# print(f'The duplicate users are: {users_duplicate}')

# data = [1,2,2,3,4,4,5]
# unique_numbers = set()

# for i in data:
#     if i not in unique_numbers and i % 2 == 0:
#         unique_numbers.add(i)

# print(f'The unique even numbers are: {unique_numbers}')


# events = ["login", "logout", "login", "compra", "login"]
# repeated_events = set()
# dont_repeated_events = set()


# for i in events:
#     if i in dont_repeated_events:
#         repeated_events.add(i)
#         print(f'The event was repeated: {repeated_events}')
#     else:
#         dont_repeated_events.add(i)
    

# list_one = [1,2,3,4,5]
# list_two = [2,4,6,8]
# list_tree = [1,3,5,7]
# elements_appear_in_lists = set()

# set_list_one = set(list_one)
# set_list_two = set(list_two)
# set_list_tree = set(list_tree)

# union_one = set_list_one & set_list_two
# union_two = set_list_one & set_list_tree
# union_tree = set_list_two & set_list_tree

# result  = union_one|union_two|union_tree

# print(f'The elements that appear in at least two lists: {result}')


# data = ["ana","luis","ana"]
# duplicates = []
# no_duplicates = set()


# for i in data:
#     if i in no_duplicates:
#         duplicates.append(i)
#     else:
#         no_duplicates.add(i)

# print(f'The numbers duplicates are: {duplicates}')


# allowed = {"admin", "users"}
# tickets = ["admin","guest","users"]
# not_allowed = set()


# for i in tickets:
#     if i in allowed:
#        print(f'access granted: {i}')
#     else:
#         not_allowed.add(i)
#         print(f'access denied: {i}')


# users = ["Ana", "Luis", "Ana", "Pedro"]
# records = set()
# duplicates = []

# for i in users:
    
#     if i not in records:
#         records.add(i)
#     else:
#         duplicates.append(i)

# print(f'Users added are: {records}')
# print(f'Users duplicates are: {duplicates}')


# alloweds = {"x1","x2","x3"}
# tickets = ["x1","x4","x2","x1","x3","x2"]

# not_alloweds = []
# duplicates = []
# valid = set()


# for i in tickets:
#     if i not in alloweds:
#         not_alloweds.append(i)

#     if i in alloweds:
#         if i in valid: 
#             duplicates.append(i) 
#         else: 
#             valid.add(i)

# print(f'Invalid data is: {not_alloweds}')
# print(f'Duplicate data is: {duplicates}')
# print(f'Valid data is: {valid}')


# data = [1,2,2,3,3,4]

# data_set = set(data)
# for_set = set()

# for i in data:
#     if i not in for_set:
#         for_set.add(i)

# print(f'Direct cleaning with the set: {data_set}')
# print(f'Cleaning of path for+set: {for_set}')


# data = [3,1,2,1,3,4]
# duplicate_list = []
# clean_list = []
# set_list = set()

# for i in data:
#     if i not in set_list:
#         clean_list.append(i)
#         set_list.add(i)
#     else:
#         duplicate_list.append(i)


# print(f'Clean list: {clean_list}')
# print(f'The list with duplicates is: {duplicate_list}')


# data = [1,2,2,3,4,4,5,1,6]

# seen_data = set()
# eliminate_duplicates = []
# save_duplicates = []


# for i in data:
#     if i in seen_data:
#         save_duplicates.append(i)
#     else:
#         seen_data.add(i)
#         eliminate_duplicates.append(i)

# print(f'The list without duplicates is {eliminate_duplicates}')
# print(f'The list with the saved duplicates is: {(save_duplicates)}')


# events = ["login","login","logout","login","logout"]

# seen_events = set()
# clean_events = []
# duplicate_events = []

# for i in events:
#     if i in seen_events:
#         duplicate_events.append(i)
#     else:
#         seen_events.add(i)
#         clean_events.append(i)

# print(f'The duplicates events is: {duplicate_events}')
# print(f'The clean events are: {clean_events}')


# events = ["login", "logout", "login", "compra", "logout"]

# seen_events = set()
# not_duplicate_events = []
# duplicates_events = []


# for i in events:
#     if i not in seen_events:
#         seen_events.add(i)
#         not_duplicate_events.append(i)
#     else:
#         duplicates_events.append(i)

# print(f'The clean events without duplicate: {not_duplicate_events}')
# print(f'duplicate events in the program: {duplicates_events}')


# users = ["u1","u2","u3","u4","u5"]
# lockedout_users = ["u2","u4"]

# set_lockedout_users = set(lockedout_users)
# valids_users_seen = set()
# valids_users = []

# for i in users:
#     if i in set_lockedout_users:
#         print(f'The user who is blocked is: {i} ')    
#     else:
#         valids_users_seen.add(i)
#         valids_users.append(i)
        

# print(f'The valid users are: {valids_users}')


# data = [1,2,2,3,4,4,5,3,6]

# seen_clean_list = set()
# clean_list = []
# duplicate_list = []

# for i in data:
#     if i in seen_clean_list:
#         duplicate_list.append(i)
#     else:
#         seen_clean_list.add(i)
#         clean_list.append(i)

# print(f'The clean and ordered list is: {clean_list}')
# print(f'The data duplicate in the list is: {duplicate_list}')


# valids_data = ["a","b","c","d"]
# data_enter = ["a","e","b","a","c","f"]

# seen_valids_data = set()
# set_valids_data = set(valids_data)
# invalid_data = []
# valids_data_ok = []
# duplicate_data = []


# for i in data_enter:
#     if i not in set_valids_data:
#         invalid_data.append(i)
#     else:
#         if i in seen_valids_data:
#             duplicate_data.append(i)
#         else:
#             seen_valids_data.add(i)
#             valids_data_ok.append(i)

# print(f'The valid data enter is: {valids_data}')
# print(f'The duplicate date enter is: {duplicate_data}')
# print(f'The invalid data enter is: {invalid_data}')


# logs = ["login","login","logout","login","logout","logout"]

# seen_logs = set()
# clean_logs = []
# duplicate_logs = []

# for i in logs:
#     if i in seen_logs:
#         duplicate_logs.append(i)
#     else:
#         seen_logs.add(i)
#         clean_logs.append(i)

# if "login" in seen_logs:
#     print("True")
# else:
#     print("False")


# print(f'The cleans logs in system are: {clean_logs}')
# print(f'The duplicates logs in system are: {duplicate_logs}')


# data = [1,2,3,2,4,5,1,6,3,7]

# seen_data = set()
# clean_data = []
# duplicates_data = []


# for i in data:

#     if i in seen_data:
#         duplicates_data.append(i)
#     else:
#         seen_data.add(i)
#         clean_data.append(i)

# print(f'The clean data are: {clean_data}')
# print(f'The duplicates data are: {duplicates_data}')


# data = [1,2,3,2,4,1]

# seen_datos = set()
# duplicate_data = []

# for i in data:
#     if i in seen_datos:
#         duplicate_data.append(i)
#     else:
#         seen_datos.add(i)

# print(f'Data duplicates is: {duplicate_data} ')


# data = [3,1,2,1,3,4]

# no_repeat_data = set()
# clean_data = []

# for i in data:
#     if i not in no_repeat_data:
#         no_repeat_data.add(i)
#         clean_data.append(i)

# print(f'The list without duplicate and order is: {clean_data}')


# a = [1,2,3,4]
# b = [3,4,5,6]

# set_a = set(a)
# set_b = set(b)

# intersec = set_a & set_b
# difference_one = set_a - set_b
# difference_two = set_b - set_a

# print(f'The itersection of a and b is: {intersec}')
# print(
#     f'The difference between a and b is: {difference_one}',
#     f'The difference between b and a is: {difference_two}'
#     )


# users = ["ana","luis","ana","pedro","luis"]

# seen_register_users = set()
# register_user = []
# users_duplicate = []

# for i in users:
#     if i not in seen_register_users:
#         register_user.append(i)
#         seen_register_users.add(i)
#     else:
#         users_duplicate.append(i)

# print(f'The users registers are: {register_user}')
# print(f'The duplicate users are: {users_duplicate}')


# numbers = [1,2,2,3,4,4,5]

# seen_register_numbers = set()
# register_numbers = []
# numbers_ignore = []

# for i in numbers:
#     if i not in seen_register_numbers:
#         register_numbers.append(i)
#         seen_register_numbers.add(i)
#     else:
#         numbers_ignore.append(i)

# print(f'The users registers are: {register_numbers}')
# print(f'The duplicate users are: {numbers_ignore}')



# events = ["login","login","logout","login","logout"]

# seen_events_order = set()
# events_order = []
# events_duplicate = []

# for i in events:
#     if i in seen_events_order:
#         events_duplicate.append(i)
#         continue

#     seen_events_order.add(i)
#     events_order.append(i)


# print(f'The events duplicates are: {events_duplicate}')
# print(f'The cleaner list of events are: {events_order}')


# data = [1,2,2,3,3,3,4,4,4,4,5] 

# valor = []
# count = []
# unique_valor = []
# two_valor = []
# more_than_valor = []

# for i in data:

#     if i not in valor:
#         count.append(1)
#         valor.append(i)
#     else:
#         position = valor.index(i)
#         count[position] += 1
    

# for i in range(len(valor)):

#     if count[i] == 1:
#         unique_valor.append(valor[i])
#     elif count[i] == 2:
#         two_valor.append(valor[i])
#     else:
#         more_than_valor.append(valor[i])


# data = ["a","b","a","c","d","c","e","b","f"]

# seen_data = set()
# unique_data = []
# duplicate_data = []
# count_data = []
# final_list = []


# for i in data:
#     if i not in seen_data:
#         seen_data.add(i)
#         unique_data.append(i)
#         count_data.append(1)
#     else:
#         position = unique_data.index(i)
#         count_data[position] += 1

# for i in range(len(unique_data)):
    
#     value = unique_data[i]
#     count = count_data[i]

#     if count > 1:
#         duplicate_data.append(value)
    
#     if count <= 2:
#         final_list.append(value)
    
# print(f'Clean data is: {final_list}')
# print(f'Duplicate data is: {duplicate_data}')


# allowed = {"x1","x2","x3","x4"}
# data_entered = ["x1","x5","x2","x1","x3","x6","x2"]

# seen_allowed = set()
# valid_allowed_data = []
# valid_duplicate_data = []
# invalid_data = []

# for i in data_entered:
#     if i not in allowed:
#         invalid_data.append(i)
#     else:
#         if i in seen_allowed:
#             valid_duplicate_data.append(i)
#         else:
#             seen_allowed.add(i)
#             valid_allowed_data.append(i)

# print(f'The allowed data is: {valid_allowed_data}')
# print(f'The allowed duplicate data is: {valid_duplicate_data}')
# print(f'The invalid data is: {invalid_data}')


# a = [1,2,3,4,5,6]
# b = [4,5,6,7,8]
# c = [5,6,9,10]
# d = a + b + c

# set_d = set(d)
# at_least_two = []
# exactly_one = []
# all_three = []
 
# for i in set_d:

#     in_a = i in a
#     in_b = i in b
#     in_c = i in c

#     count = in_a + in_b + in_c 

#     if count >= 2:
#         at_least_two.append(i)
#     if count == 1:
#         exactly_one.append(i)
#     if count == 3:
#         all_three.append(i)
    
    
# print(f'The numbers that appear in a single list are: {exactly_one} ')
# print(f'The numbers that appear in at least two lists are: {at_least_two} ')
# print(f'The numbers that appear in the three lists are: {all_three} ')



# events = ["login","error","login","warning","error","login","logout"]

# seen_events = set()
# final_list = []


# for i in events:
#     if i == "error":
#         final_list.append(i)
#     elif i == "login":
#         if i not in seen_events:
#             final_list.append(i)
#             seen_events.add(i)
#         else:
#             continue
#     else:
#         if i not in seen_events:
#             seen_events.add(i)
#             final_list.append(i)
#         else:
#             continue

# print(f'The clean data are: {final_list}')


# data = [10,15,10,20,25,20,30,35,30]

# seen_data = set()
# unique_data = []
# unique_even = []

# duplicate_odd = []

# final_list = []
# count_data = []

# for i in data:
    
#     if i not in seen_data:
#         seen_data.add(i)
#         count_data.append(1)
#         unique_data.append(i)
#     else:
#         position = unique_data.index(i)
#         count_data[position] += 1
    
# for i in range(len(unique_data)):

#     count = count_data[i]
#     value = unique_data[i]

#     if count == 1:
#         if value % 2 == 0:
#             unique_even.append(value)
#             final_list.append(value)

#     if count > 1:
#         if value % 2 == 1:
#             duplicate_odd.append(value)
    
# print(f'The data in final list are: {final_list}')

# data = [["comida",10],["comida",20],["transporte",5],
#        ["comida",10],["transporte",5],["salud",50]]

# seen_category = set()
# category = []

# duplicate_group = []

# final_group = []
# new_group = []
# group = []

# for i in range(len(data)):

#     if data[i][0] not in seen_category:
#         seen_category.add(data[i][0])
#         category.append(data[i][0])
#         group.append([data[i][1]])
#     else:
#         position = category.index(data[i][0])
#         group[position].append(data[i][1])

# for i in group:

#     seen_group_one = set()
#     seen_duplicate = set()
#     duplicate = []

#     for j in i:
#         if j not in seen_group_one:
#             seen_group_one.add(j)
#         else:
#             if j in seen_duplicate:
#                 continue
#             else:
#                 seen_duplicate.add(j)
#                 duplicate.append(j)
#     duplicate_group.append(duplicate)

# for i in range(0,len(category)):
#     final_group = [category[i],duplicate_group[i]]
#     new_group.append(final_group)


# users = ["u1","u2","u3","u1","u4","u2","u5","u3"]
# blocked = {"u2","u5"}

# seen_users = set()
# seen_duplicate = set()
# valid_duplicate_users = []
# final_list = []
# valid_users = []

# for i in users:
#     if i in blocked:
#         continue
#     else:
#         valid_users.append(i)        

# for i in valid_users:
#     if i not in seen_users:
#         seen_users.add(i)
#         final_list.append(i)
#     else:
#         if i not in seen_duplicate:
#             seen_duplicate.add(i)
#             valid_duplicate_users.append(i)
#         else:
#             continue

        

# print(f'The valid users in users: {final_list}')


# day1 = [1,2,3,4]
# day2 = [3,4,5,6]
# day3 = [4,5,6,7]

# concatenation_lists = day1 + day2 +day3
# set_concatenation = set(concatenation_lists)

# disappear_one = []
# disappear_two = []
# persistent_elements = []
# new_day2 = []
# new_day3 = []

# for i in set_concatenation:
    
#     in_day1 = i in day1
#     in_day2 = i in day2 
#     in_day3 = i in day3

#     if in_day1 and not in_day2:
#         disappear_one.append(i)
#     if in_day2 and not in_day3:
#         disappear_two.append(i)

#     if in_day1 and in_day2 and in_day3:
#         persistent_elements.append(i)

#     if not in_day1 and in_day2:
#         new_day2.append(i)
#     if not in_day2 and in_day3:
#         new_day3.append(i)

# print(f'Numbers disappers day 2 are: {disappear_one}')
# print(f'Numbers disappers day 3 are: {disappear_two}')
# print(f'Numbers persistents in 3 day: are: {persistent_elements}')
# print(f'The new numbers in day 2 are: {new_day2}')
# print(f'The new numbers in day 3 are: {new_day3}')


# data = ["a","b","a","c","d","c","e","b","f","g","a"]
# allowed = {"a","b","c","d","e"}

# seen_duplciate = set()
# duplicate_unique = []
# seen_valid = set()
# unique_valid = []
# invalid = []


# for i in data:
#     if i in allowed:
#         if i not in seen_valid:
#             seen_valid.add(i)
#             unique_valid.append(i)
#         else:
#             if i in seen_duplciate:
#                 continue
#             else:
#                 seen_duplciate.add(i)
#                 duplicate_unique.append(i)
#     else:
#         invalid.append(i)

# print(f'The only valid data are: {unique_valid}')
# print(f'The only duplicate data are: {duplicate_unique}')
# print(f'The only invalid data are: {invalid}')


# logs = ["login","login","error","login","error","logout","logout","login"]

# seen_logs = set()
# final_logs = []
# last_event = None

# for i in logs:
#     if i == "error":
#         final_logs.append(i)
#     elif i == "login":
#         if i not in seen_logs:
#             seen_logs.add(i)
#             final_logs.append(i)
#     elif i == "logout":
#         if last_event != "logout":
#             final_logs.append(i)
#     last_event = i
        

# print(final_logs)


# data = [1,2,2,3,4,4,5,6,6,7,8,8,9,10,10,10]

# counts = []
# seen_data = set ()

# data_one = []
# duplicate_data = []
# data_more_two = []
# unique_data = []

# for i in data:

#     if i not in seen_data:
#         counts.append(1)
#         seen_data.add(i)
#         data_one.append(i)
#     else:
#         position = data_one.index(i)
#         counts[position] += 1

# for i in range(len(data_one)):
#     if counts [i] == 1:
#         unique_data.append(data_one[i])
#     if counts[i] >= 2:
#         duplicate_data.append(data_one[i])
#     if counts[i] > 2:
#         data_more_two.append(data_one[i])

# for i in data_one:
#     pass


# print(f'The list of unique data is: {unique_data}')
# print(f'The list of duplicate data is: {duplicate_data}')
# print(f'the list where numbers appear repeated more than twice: {data_more_two}')
