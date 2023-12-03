# CS515 Project 2 - Adventure
- Ali El Sayed aelsaye1@stevens.edu
- https://github.com/A-El-Sayed/CS515-Project2-Adventure
- I spent about 5 hours on this project
- The way i tested my code was by debugging my code and using breakpoints by each line of code to ensure that each line was doing whats it meant to do.
- I have no bugs in my code
- i had an issue with implementing the help verb as i wasn't sure how i would implement it without using static code. However i was able to solve it using dir(self) and took out the added verbs and then added them to the list of verbs

## Extensions
### help
- how to use help. I ended up using dir(self) to get all the created verbs instead of just printing static text
```
What would you like to do? help
```
- Expected output
  ```
  You can run the following commands:
    drop ...
    get ...
    go ...
    help
    inventory
    look
    pick ...
    quit
  ```

  ### drop
- how to use drop.
```
What would you like to do? drop [item]
```
- Expected output
  ```
  You drop the [item].
  ```

  ### pick: Interaction Extension
- there is a certain item "diamond" that can't be gotten using the 'get' verb since it is locked in a safe that needs to be locked. In order to unlock the safe, you use the verb 'pick', which will require that you answer a couple of riddles in order to unlock the safe and immediately add the diamond to your inventory. Once the "diamond is added to inventory" it is then treated as a normal item where you can drop it in any room and lock it again.
- How to use pick.
```
What would you like to do? pick [item]
```
- Expected output. Feel free to answer the question wrog each time in order to see what the output will be.
  ```
  You'll need to answer riddles in order to unlock the safe (ONE-WORD-ANSWERS)
  1) What's something that has a head and a tail, but no body (hint: think round objects)? coin

  Thats the right answer! Next one is a little harder though
  2) If you have me, you will want to share me. If you share me, you will no longer have me. What am I? secret

  Correct again! Okay, this is it. FINAL riddle.
  3) I follow you all the time and copy your every move, but you can't touch or catch me. What am I? shadow

  Alright! Alright! Here! You deserve it.
  You pick up the diamond.
  ```
