class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"
    def hand_list(self,philosopher,book):
        print(f"{philosopher} wrote the book: {book}")
    
whodunnit = MyFirstClass()
print(whodunnit.index)
whodunnit.hand_list("Sun Tzu","The Art of War")