class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lista = (nums1+nums2)
        lista.sort()
        tamanho_lista = len(lista)
        if tamanho_lista%2 == 0:
            return sum(lista[(tamanho_lista//2)-1:(tamanho_lista//2)+1:])/2
        else:
            return lista[tamanho_lista//2]
