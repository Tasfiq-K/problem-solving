## The Problem
**[Count Number of Homogenous Substrings](https://leetcode.com/problems/count-number-of-homogenous-substrings/description/?envType=daily-question&envId=2023-11-09)**

Given a string `s`, return the number of **homogenous** **substrings** of `s`. Since the answer may be too large, return it modulo $10^9 + 7$. So, what does **homogenous** mean? A string is called **homogenous** if all the characters of the string are the same. For example, "ssss" a string which contains only the character "s" which are the same is called a **homogenous** string. 

Now, what's a **substring**? It's contiguous sequence of characters within a string. For example, "cat sat on" in the words "The cat sat on the mat" can be called a substring. Also, "bbb" in the string "abcbbbdd" can be thought as a substring. Now for the second example, the "bbb" substring can also be called a **Homogenous Substring**. Because, it is a contguous sequence and the characters are all same. 

Now, the goal here is to count all the homogenous substrings and add them up, then return the summation. 

An explanation from the problem description is as follows: <br>
Input: s = "abbcccaa" <br>
Output: 13 <br>
Explanation: The homogenous substrings are listed as below: <br>
"a"   appears 3 times.<br>
"aa"  appears 1 time.<br>
"b"   appears 2 times.<br>
"bb"  appears 1 time.<br>
"c"   appears 3 times.<br>
"cc"  appears 2 times.<br>
"ccc" appears 1 time.<br>
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

One thing to note here, a single character in string is also a (you got it) **homogenous substring**

## The Approach
We count the number of times we encounter a contiguous homegenous substring and sum them up
"a" = 1 "a", we encounter 1, so our count is 1 <br>
"bb" = 2 "b", we count 1 when we encounter the first "b" then when we encounter the 2nd "b" we count 2 and sum the values so (1 + 2) = 3 <br>
"ccc" = 3 "c", considering the prvious counting technique, this will be (1 + 2 + 3) = 6 <br>
"aa" = This will also be (1 + 2) = 3. Now summing all these up will give us, (1 + 3 + 6 + 3) = 13, which is our result. <br>

Anohter way you can think is that you are calculating the sum of n continuous number, in that case the formula is: $\frac{n(n+1)}{2}$ where `n` is the total count of a homogenous continuous string. For example, for the substring "ccc", we have total count of 3. So, by the summation rule we get $\frac{3*(3+1)}{2} = 6$

So let's go over the procedure:

* Create counting variables, say `ans` for summing all the results, and `curr_streak` for continuous summing streak and initialize them with 0
* Create a `mod` variable to hold the modulo constant
* Now, iterate over the length of string:
    * If the current index is 0 or the letter of current index and the previous index are same, then
        * increment the `curr_streak`
    * Else, 
        * assign 1 to the `curr_streak`. So, we re-initialize for the new character.
    * Update `ans` = `ans`+ `curr_streak` % `mod`
* Return `ans`

## The Code

```python
class Solution:
    def countHomogenous(self, s: str) -> int:
        # creating the variables
        ans = 0 
        curr_streak = 0
        MOD = 10 ** 9 + 7

        length = len(s)

        for indx in range(length): # iterate over the length of the string
            if indx == 0 or s[indx] == s[indx - 1]: # if index = 0 or if current index = prev index, increment curr_streak
                curr_streak += 1
            else:
                curr_streak = 1 # else, re-initialize curr_streak for new character
        
            ans = (ans + curr_streak) % MOD # Total sum up to the current index position
         
        return ans

```
