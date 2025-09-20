#Assignment operator vs shallow copy vs deep copy

#Assignment operator
list1=[1,2,[3,4]]
list2=list1         #assignment (no copy)
list2[0]=100
print(list1)     #[100,2,[3,4]]

#shallow copy
import copy
list1=[1,2,[3,4]]
list2=copy.copy(list1)   #shallow copy
list2[0]=100
list2[2][0]=200
print(list1)           #[1,2,[200,4]]      nested list affected
print(list2),          #[100,2,[200,4]]

#deep copy
list1=[1,2,[3,4]]
list2=copy.deepcopy(list1)      #deep copy
list2[0]=100
list2[2][0]=200
print(list1)            #[1,2,[3,4]]         unaffected
print(list2)            #[100,2,[200,4]]

