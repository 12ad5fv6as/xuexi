rows = [{"pid": 1,"rss": 20},{"pid":2,"rss":50}]
ordered = sorted(rows,key= lambda item: item["rss"],reverse=True) 
print(ordered[:1])
