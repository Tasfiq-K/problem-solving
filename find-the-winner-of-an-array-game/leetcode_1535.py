class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # counter = defaultdict(int)

        # if k > len(arr):
        #     return max(arr)

        # while k not in counter.values():
        #     if arr[0] > arr[1]:
        #         counter[arr[0]] += 1
        #         loser = arr.pop(1)
        #         arr.append(loser)
                
        #     else:
        #         counter[arr[1]] += 1
        #         loser = arr.pop(0)
        #         arr.append(loser)
        
        # return arr[0]

        # count = 0

        # while count != k:
        #     if arr[1] > arr[0]:
        #         count = 1
        #         loser = arr.pop(0)
        #         arr.append(loser)
                
        #     else:
        #         count += 1
        #         if count == k:
        #             break
        #         loser = arr.pop(1)
        #         arr.append(loser)

        # return arr[0]

        if k > len(arr):
            return max(arr)

        count = 0
        winner = arr[0]
        arr_length = len(arr)

        for idx in range(1, arr_length):
            if arr[idx] > winner:
                winner = arr[idx]
                count = 1
            else:
                count += 1
            
            if count == k:
                # return winner
                break
        
        return winner
        


        
