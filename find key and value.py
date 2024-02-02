my_dict={}
while True:
    key=input("key:(end結束)")
    if key=="end":
        break
    value=input("value:")
    my_dict[key]=value
search_key=input("Search key or value:")
if search_key in my_dict.keys():
    print(f"Yes, {search_key} is a key")
    print(f"your search key about the value is {my_dict[search_key]}")
elif search_key in my_dict.values():
    print(f"Yes, {search_key} is a value")