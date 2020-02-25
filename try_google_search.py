from google import google


search = input("Enter query: ")
page_num = 1

results = google.search(search, page_num)

for res in results:
    print(res)



