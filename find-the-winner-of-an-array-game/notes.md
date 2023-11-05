## The Problem
**[Find The Winner of An Array Game](https://leetcode.com/problems/find-the-winner-of-an-array-game/?envType=daily-question&envId=2023-11-05)**

The problem is pretty straight forward. A game will be played among the elements of an array (list). Where the partcipants will be the first two elements of the array `arr[0]` and `arr[1]`. The winner will be the one who wins `k` times. `k` is an integer and will be provided. The values will be distinct and there will be surely an winner. Now, How do we determine how the participant will win `k` times. Well, at each round you're gonna have to compare the first two elements of the array, the larger one goes to the 0th position and the smaller goes to the end of the list, the game continues until any participant wins `k` time consecutively. Easy, right?! But again, this is a `medium` level probelm. However, let's see the approaches.

## The approach
A lot of approaches can be taken to solve this problem. The first approach I took was naive one. It did well, in the memory usage department, but not so good in runtime. However, I came up with other solutions, also slightly modified few existing ones.

### My approach

My initial approach was simple. 
* You create a counter dictionary, where you store each element in the list as a key, and the number of times they win as values.
* Now loop over the elements in the array until you found the values in the dictionary equals to `k`.
* When looping over the elements, you compare the `arr[0]` and `arr[1]`
    * if `arr[0]` > `arr[1]` -> `arr[0]` stays at its position, `arr[1]` goes to the end.
    * else -> `arr[1]` moves to 0th position and `arr[0]` goes to the end.

    * Also, you count the number of times each elements win and store them in the counter dictionary as values and the elements as the key.

* When `k` is found, you terminate the loop, and then loop over the counter dictionary to get the key who has the value `k` and return the key.
    * Modification of this approach is, as you change you elements position each time in the loop, so when the winner is found, that has to be the first element in the array. Since It stayed there for `k` consecutive times. So, you just return the first element `arr[0]` as the winner.

Now, this approach is naive one, and takes a lot of time, more than 4000 ms. So, we should optimize it. The next approach we observe is optimal one, at least comparing this one.

## Optimal Approach
This approach iterates over the given array using a for loop

* First we check if `k` > length of the array, then we simply return the maximum number of the array.
* If that's not the case, then we iterate over the indexes of the elements from index position 1 to the length of the array. We create a variable called `winner` to keep track of the number, we initialize the variable wiht the first element, so, `winner = arr[0]`. We also create the counter variable.
* So, for each positional element we compare the current `winner` with the positional element. 
    * If the positional element is greater then we make it the winner, and assign 1 to the counter 1, and then check if counter is equal to the given `k`, if it is then we break out the loop and return the current winner. If not we continue looping.
    * Else, we keep the winner as it was and increase the counter, and check if the counter is equal to the given `k`. If it is we break the loop, and return the current winner. Else, we keep looping.

## The Code

## My Approach

```python
        counter = defaultdict(int)

        if k > len(arr):
            return max(arr)

        while k not in counter.values():
            if arr[0] > arr[1]:
                counter[arr[0]] += 1
                loser = arr.pop(1)
                arr.append(loser)
                
            else:
                counter[arr[1]] += 1
                loser = arr.pop(0)
                arr.append(loser)
        
        return arr[0]

```

## Optimal Appraoch

```python
        if k > len(arr): # if the number of consecutive wins is greater than the length of the array, return the maximum number of the array as the answer. Well, give it a thought.
            return max(arr)

        count = 0 # create the counter variable
        winner = arr[0] # initial winner
        arr_length = len(arr) 

        for idx in range(1, arr_length): # iterate over the loop from 1 to its final length
            
            if arr[idx] > winner: # if the current index is greater than make it current winner
                winner = arr[idx]
                count = 1 # assign counter to 1, so for every new winner the counter will re-initialize
            
            else: # for consecutive win, increase the counter
                count += 1
            
            if count == k: # check at every iteration
                break
        
        return winner
        
```