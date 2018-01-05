if __name__ == '__main__':
    list_outer = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_inner = [name, score]       
        list_outer.append(list_inner)
    
    # This finds min and max
    Min = 100
    Max = 0
    for item in list_outer:
        if item[1] > Max:
            Max = item[1]
            print("Min", Min)
        if item[1] < Min:
            Min = item[1]
            print("Max", Max)
    ##        
    """
    Sec_lowest = Max
    for item in list_outer:
    	if item[1] > Min and item[1] <= Sec_lowest:
          Sec_lowest = min(item[1])
          name = item[0]
    print(Sec_lowest, name)
"""
