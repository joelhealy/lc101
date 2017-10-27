

Solve the following non-coding problem to practice your problem solving skills.

A farmer is on his way to market with a fox, a chicken, and a bag of corn. He
must cross a river to get there. On the bank of the river is a boat that is big
enough only for the farmer and one additional item, so he must take the three
across one at a time.

    *  If the farmer takes the fox first, the chicken will eat the corn.
    *  If the farmer takes the corn first, the fox will eat the chicken.
    *  If the farmer takes the chicken first, the fox will not eat the corn.
       However, he’ll then have to take either the fox or corn on the next
       trip, and when left alone to return for the final item one of the first
       two situations will occur.

How can the farmer get all three across without losing one?


Answer:

River Bank 1     |  Boat in River       |  River Bank 2
-----------------|----------------------|--------------
farmer, fox, chicken, corn  |           |
fox, corn        | farmer, chicken -->  |
fox, corn        | <-- farmer           | chicken
corn             | farmer, fox -->      | chicken
corn             | <-- farmer, chicken  | fox
chicken          | farmer, corn -->     | fox
chicken          | <-- farmer           | fox, corn
                 | farmer, chicken -->  | fox, corn
                 |                      | farmer, fox, chicken, corn
