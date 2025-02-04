if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #.split() - used to split a string by default space
    #map(function, iterables) - later we can convert this map() to any data structure
    

    #code here
    unique_scores = sorted(set(arr), reverse=True)
    #set() - convert data set into set
    #sorted(data_structure, condition if necessary) - to sort a data structure
                #doesnt change the order of data structure
                #it just outputs the sorted data structure
    #reverse = True - reverses the sorted data structure
    print(unique_scores[1])
