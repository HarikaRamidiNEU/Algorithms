import copy
import time
import generate_Supergroup1 as generateSG1
import generate_supergroup2 as generateSG2
start = time.time()

def check(matches, SG1, SG2):
    inversematches = dict((v,k) for k,v in matches.items())
    for sg2team, sg1team in matches.items():
        SG2teampreference = SG2[sg2team]
        SG2teambetterpreference = SG2teampreference[:SG2teampreference.index(sg1team)]
        SG1teampreference = SG1[sg1team]
        SG1teambetterpreference = SG1teampreference[:SG1teampreference.index(sg2team)]
        for SG1team in SG2teambetterpreference:
            SG1teamCurrent = inversematches[SG1team]
            guylikes = SG1[SG1team]
            if guylikes.index(SG1teamCurrent) > guylikes.index(sg2team):
                return False
        for SG2team in SG1teambetterpreference:
            SG2teamCurrent = matches[SG2team]
            SG2teamlikes = SG2[SG2team]
            if SG2teamlikes.index(SG2teamCurrent) > SG2teamlikes.index(sg1team):
                return False
    return True

def matchmaker(SG1, SG2):
    SG1teams = sorted(SG1.keys())
    SG1teamsfree = SG1teams[:]
    matches  = {}
    SG12 = copy.deepcopy(SG1)
    SG22 = copy.deepcopy(SG2)
    while SG1teamsfree:
        SG1team = SG1teamsfree.pop(0)
        SG1teamslist = SG12[SG1team]
        SG2team = SG1teamslist.pop(0)
        playbuddyteam = matches.get(SG2team)
        if not playbuddyteam:
            # SG2 team's free
            matches[SG2team] = SG1team
        else:
            # The bounder proposes to an matches lass!
            SG2teamslist = SG22[SG2team]
            if SG2teamslist.index(playbuddyteam) > SG2teamslist.index(SG1team):
                # SG2team prefers new SG1team
                matches[SG2team] = SG1team
                if SG12[playbuddyteam]:
                    SG1teamsfree.append(playbuddyteam)
            else:
                # SG2team is faithful to old playbuddyteam
                if SG1teamslist:
                    # Look again
                    SG1teamsfree.append(SG1team)
    return matches

SG1 = generateSG1.generate(8)
SG2 = generateSG2.generate(8)

matches = matchmaker(SG1, SG2)

print('\n Matches:')
print('  ' + ',\n  '.join('%s plays with %s' % couple
                          for couple in sorted(matches.items())))
print()
print('Playoffs stability check PASSED'
      if check(matches, SG1, SG2) else 'Playoffs stability check FAILED')

end = time.time()
print('Total time of execution for 8 teams in each super group is ',(end - start))

# shuffling 1000 times each pair to calculate the percentage of stable playoff matches
success = 0
for i in range(1000):
   SG1 = generateSG1.generate(8)
   SG2 = generateSG2.generate(8)
   matches = matchmaker(SG1, SG2)
   if(check(matches, SG1, SG2)):
        success+=1
        if(success == 1000):
            break
print()
print('The percentage of stable playoff matches after shuffling each team preference for 1000 times is ', (success/1000)*100)


start = time.time()

SG1 = generateSG1.generate(16)
SG2 = generateSG2.generate(16)

print('\n Playoffs:')
matches = matchmaker(SG1, SG2)

print('\n Matches:')
print('  ' + ',\n  '.join('%s plays with %s' % couple
                          for couple in sorted(matches.items())))
print()
print('Playoffs stability check PASSED'
      if check(matches, SG1, SG2) else 'Playoffs stability check FAILED')

end = time.time()
print('Total time of execution for 16 teams in each super group is ',(end - start))



start = time.time()

SG1 = generateSG1.generate(32)
SG2 = generateSG2.generate(32)

print('\n Playoffs:')
matches = matchmaker(SG1, SG2)

print('\n Matches:')
print('  ' + ',\n  '.join('%s plays with %s' % couple
                          for couple in sorted(matches.items())))
print()
print('Playoffs stability check PASSED'
      if check(matches, SG1, SG2) else 'Playoffs stability check FAILED')

end = time.time()
print('Total time of execution for 32 teams in each super group is ',(end - start))