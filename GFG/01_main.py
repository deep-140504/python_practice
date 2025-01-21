test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
cus_eles = [6, 7, 8]
print("list before operation is: ", str(test_list))
test_list = [[(idx + (val , )) for idx in key] for key, val in zip(test_list, cus_eles)]
print("list after operation is: ", str(test_list))

temp = [[(idx + (val, )) for idx in key] for key, val in zip(test_list, cus_eles)]
print()