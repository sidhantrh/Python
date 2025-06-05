def append_to_list(val, lst):
    for i in lst:
      if i == val:
        continue
      else:
        lst.append(val)
    return lst

lst = [1,2,3,4]
print(append_to_list(5,lst))