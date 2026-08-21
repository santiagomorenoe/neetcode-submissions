class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumaE = n * (n+1) // 2
        sumaR = sum(nums)
        return sumaE - sumaR

        
            #Solución optima, sin recorrer arreglos ni memoria extra
            #time: O(n)
            #space: O(1)
        

         
            #Solución 2 (ineficiente): 
            #ordenada = sorted(nums) 
            #for i,n in enumerate(ordenada): 
            #    if i != ordenada[i]: 
            #return i return len(ordenada) 
            
            #sorted() = O(n log n) = crea una nueva lista en memoria 
            #time: O(n log n) space: O(n) 