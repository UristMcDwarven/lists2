scores = [88, '92', 78, 90, 98, 84]
print(scores)
for x in scores:
    print(x)
has92 = '92' in scores
print(has92)
has89 = '89' in scores
print(has89)
print(len(scores))

scores.append('81')
print(scores)

score = '85'
scores.insert(0, score)
print(scores)


quest_slot = ['nostone']
has_stone = 'stone' in quest_slot
print(has_stone, 'you do not have the stone')
no_stone = 'nostone' in quest_slot
print(no_stone, 'You have the stone')
if has_stone == False:
    print('has stone false')

chest = ['spellbook', 'knife', 'gold_coin']
scores.extend(chest)

print(scores)

scores.remove('knife')
print(scores)

print(chest)
chest.pop(1)
print(chest)

chest.sort()
chest.reverse()
print(chest)

chest_copy = chest.copy()
print(chest_copy)

chest_copy.append('brown')
print(chest_copy)
print(chest)
chest.append('alpha')
chest.sort()
print(chest)
things_popped = chest.pop(1)
print(things_popped)
print(chest)



