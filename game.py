letters = [['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm','i','n','g'],

           ['h','o','l','i','d','a','y'], 

           ['b','o','o','t','c','a','m','p'],

           ['f','l','o','w','c','h','a','r','t'],

           ['w', 'o', 'r', 'd', 's', 'c', 'a','p','e','s']]

 

words = [["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",

          "pong","pram","prom","ramp","gram","ramin"], 
         
         ["hi","hay","day","had","lay","dal","lad","lid","hold","lady","hail","old","holi","daily"],

         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",

          "comb","boom","pact","atom"],

         ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",

          "fowl","wolf","crow","half"],

         ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",

          "cope","crap","crew","crop","pace"]];

lives=5  # no of chances
level=0  # no of level
score=0  # score of user

while level<5:
    
    print(f'welcome to level {level+1}')
    print('Create three meaningful words from the given letters')
    for i in letters[level]:
        print(i,end=' ')
    print()        # for showing the letters
    wordcount=0
    
    word=''
    oldword=[]
    while wordcount==0 or wordcount<3:
        match=False
        word=input('')
        if word.lower() not in oldword:
            for i in words[level]:
                if word==i:
                    wordcount=wordcount+1
                    score=score+1
                    oldword.append(word)
                    match=True
                    break
        if not match:
            print('wrong guess')
            lives=lives-1
            
        if lives==0:
            print('Game over ,Better luck next time')
            print('your score is',score)
            break
    wordcount=0
    match=False
    word=''
    oldword=[]
    
    if lives==0:
        break
    if level==4:
        print('thank you playing the game')
        print('your score ',score)
        level=level+1
    else:
        choice=input('do you want to continue to the next level (y/n)')
        if choice.lower()=='y':
            level=level+1
        else:
            print('thank you for playing the game')
            print('your score is',score)
            break         