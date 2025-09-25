#Implement a function to merge two dictionaries.

#method -1
def merge_dict(dict1,dict2):
    merged=dict1.copy()
    for key,value in dict2.items():
        merged[key]=value
    return merged
dict1={"name":"Harish"}
dict2={"Age":21}
print(merge_dict(dict1,dict2))    #if the keys are with same name in dict1 and dict2, it will take first dictionary key and value


#method-2
def merge_dicts(dict1,dict2):
    return {**dict1,**dict2}
print(merge_dicts(dict1,dict2))

#method-3
def merge_dictss(dict1,dict2):
    return dict1|dict2
print(merge_dictss(dict1,dict2))