'''
This is an example for CREATING THE REFERENCE OF EXISTING SET data structure
'''
#set
superHeroSet=set(['ironman','spiderman','superman','batman','wonder women','caption america'])
print('Set:', superHeroSet)

#creating the ref into new set object
refSuperHeroSet=superHeroSet
print('ref Set: ', refSuperHeroSet)

#Do few operations on old and copied set object
print('adding new item in refSuperHeroSet')
refSuperHeroSet.add('ant man')

print('Copied Set: ', refSuperHeroSet)
print('Original set : ', superHeroSet)