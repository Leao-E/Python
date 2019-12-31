class Solution:
    def romanToInt(self, s: str) -> int:
        dicti = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500,"M":1000}
        soma = 0
        string2 = s[::-1]
        valorAnterior = string2[0]
        for i in string2:
        	if dicti[i] >= dicti[valorAnterior]:
	        	soma += dicti[i]
	        else:
    		    soma -= dicti[i]
	        valorAnterior = i
        return(soma)		