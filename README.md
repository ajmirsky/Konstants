Konstants
=========

Originally based on a snippit that I found years ago, but can no longer find the link. 
( will be happy to give credit if someone tells me who the original author is )

Usage
=====

    MYENUMERATION = Konstants(
       K(firstconstant=0, label="first constant"),
       K(secondconstant=9, label="second constant"),
       K(thirdconstant=16, label="third constant),
    )

    >> MYENUMERATION[firstconstant]
    0

    >> # helpful for population a django ChoiceField
    >> MYENUMERATION.choices()
    [(0, u'first constant'),(9, u'second constant', 9), (16, u'third constant')]

    >> MYENUMERATION.labels()
    ('first constant', 'second constant', 'third constant')

     >> MYENUMERATION.firstconstant
     0
     >> MYENUMERATION[9]
     'second constant'
     >> MYENUMERATION[MYENUMERATION.thirdconstant]
     'third constant'
9
>> MyENUMERATION.thirdconstant
16
