from traceback import print_list


print("hello")
#print statement are written in four types that are(normal form,percentaile{%},dot format{.},f statement{f''})
#datatypes in python are string,list,tuple,dictionary(dict),set,float,boolean,integer
#print statement in string
food="briyani"
juice="chocolate milkshake"
desert="brownie"
print(food,juice,desert)
print('liked food is:',food,';favourite drink is:',juice,';needed desert is:',desert)
print('liked food is:',food,';favourite drink is:',juice,';needed desert is:',desert)
print(" liked food is %s ,favourite drink is %s ,needed desert is %s" % (food,juice,desert))
print("liked food is {} ,favourite drink is {} ,needed desert is {}" .format(food,juice,desert))
print("liked food is {2} ,favourite drink is {0} ,needed desert is {1}" .format(juice,desert,food))
print(f' liked food is {food} ,favourite drink is {juice} ,needed desert is {desert}')
print(f' liked food is {"briyani"} ,favourite drink is {"chocolate milkshake"} ,needed desert is {"brownie"}')
#print statement in integer
mark_chem="99"
mark_maths="98"
mark_phy="97"
mark_pspp="100"
print(mark_chem,mark_maths,mark_phy,mark_pspp)
print('my math mark is:',mark_maths,';my chemistry mark is:',mark_chem,';my physics mark is:',mark_phy,';my python mark is:',mark_pspp )
print("my math mark is: %s ;my chemistry mark is: %s ;my physics mark is : %s ;my python mark is: %s" %(mark_chem,mark_maths,mark_phy,mark_pspp))
print("my math mark is: {} ;my chemistry mark is: {} ;my physics mark is : {} ;my python mark is: {}" .format(mark_chem,mark_maths,mark_phy,mark_pspp))
print("my math mark is: {2} ;my chemistry mark is: {1} ;my physics mark is : {3} ;my python mark is: {0}" .format(mark_pspp,mark_chem,mark_maths,mark_phy))
print(f'my math mark is: {mark_maths} ;my chemistry mark is: {mark_chem} ;my physics mark is : {mark_phy} ;my python mark is:{mark_pspp}')
print(f'my math mark is: {98} ;my chemistry mark is: {99} ;my physics mark is : {97} ;my python mark is:{100}')
#print statement for list
list1=[]
list2=[1,2,3,4,5]
list3=['python',24,2.5]
print(list1,list2,list3)
print(list1+list2+list3)
print('list one is:',list1, ';list two is:',list2,';list three is:',list3)
print("list one is: %s ;list two is: %s ;list three is: %s" %(list1,list2,list3))
print("list one is: {} ;list two is: {} ;list three is: {}" .format(list1,list2,list3))
print("list one is: {2} ;list two is: {1} ;list three is: {0}" .format(list3,list2,list1,))
print(f'list one is: {list1} ;list two is: {list2} ;list three is: {list3}')
print(f"list one is {[]} ; list two is {[1,2,3,4,5]} ; list three is {['python',24,2.5]}")
#print statement for tuple
tuple1=('hello',11,1.05)
tuple2=(1,2,3,4)
tuple3=('python','hello','world')
print(tuple1,tuple2,tuple3)
print(tuple1+tuple2+tuple3)
print('tuple 1 is:',tuple1, ';tuple 2 is:',tuple2,';tuple 3 is:',tuple3)
print("tuple 1 is: %s ;tuple 2 is: %s ;tuple 3 is: %s" %(tuple1,tuple2,tuple3))
print("tuple 1 is: {};tuple 2 is: {} ;tuple 3 is: {}" .format(tuple1,tuple2,tuple3))
print("tuple 1 is: {1} ;tuple 2 is: {2} ;tuple 3 is: {0}" .format(tuple3,tuple1,tuple2))
print(f"tuple 1 is: {tuple1} ;tuple 2 is: {tuple2} ;tuple 3 is: {tuple3}" )
print(f"tuple 1 is: {('hello',11,1.05)} ;tuple 2 is:{(1,2,3,4)} ;tuple 3 is: {('python','hello','world')} " )
#print statement for sets
set1={1,2,3}
set2={'hello','python',24,2.5}
print(set1,set2)
print('set 1 is:',set1,';set 2 is:',set2 )
print('set 1 is: %s ;set 2 is: %s' %(set1,set2) )
print('set 1 is: {} ;set 2 is: {}' .format(set1,set2) )
print('set 1 is: {1};set 2 is: {0}' .format(set2,set1) )
print(f"set 1 is: {set1} ;set 2 is: {set2}" )
print(f"set 1 is: {{1,2,3}} ;set 2 is: {{'hello','python',24,2.5}}" )
#print statement for dictionary
dict1={'place':'lets upgade','date':'19-01-22'}
dict2={'name':'python','version':'3.9.10'}
print(dict1,dict2)
print('dictionary 1 is :',dict1,';dictionary 2 is',dict2)
print('dictionary 1 is : %s ;dictionary 2 is %s' %(dict1,dict2))
print('dictionary 1 is : {} ;dictionary 2 is {}' .format(dict1,dict2))
print('dictionary 1 is : {1} ;dictionary 2 is {0}' .format(dict2,dict1))
print(f"dictionary 1 is : {dict1} ;dictionary 2 is {dict2}")
print(f"dictionary 1 is : {{'place':'lets upgade','date':'19-01-22'}} ;dictionary 2 is {{'name':'python','version':'3.9.10'}}")
#print statement for float
english_percent=99.9
tamil_percent=99.5
maths_percent=100.0
print(english_percent,tamil_percent,maths_percent)
print('english percentage is:',english_percent,';tamil percentage is:',tamil_percent,';maths percentage is:',maths_percent)
print('english percentage is: %s ;tamil percentage is: %s ;maths percentage is:%s' %(english_percent,tamil_percent,maths_percent))
print('english percentage is: {} ;tamil percentage is: {} ;maths percentage is:{}' .format(english_percent,tamil_percent,maths_percent))
print('english percentage is: {1};tamil percentage is: {2} ;maths percentage is:{0}' .format(maths_percent,english_percent,tamil_percent,))
print(f"english percentage is: {english_percent} ;tamil percentage is: {tamil_percent} ;maths percentage is:{maths_percent}")
print(f"english percentage is: {99.9} ;tamil percentage is: {99.5} ;maths percentage is:{100.0}")
#print statement for boolean
x=5
y=10
print(bool(x==y))











