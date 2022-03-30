from pytube import Search 

search = Search(input("Enter Search Kaeyword here :\t "))
print(search.results)
print(search.result[0])