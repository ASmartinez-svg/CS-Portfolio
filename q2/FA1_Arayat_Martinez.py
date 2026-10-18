class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

  
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

   
    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self.__number_of_pages = number_of_pages

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    
    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("Issue number must be positive.")
        else:
            self.__issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.__issue_number}")


#testclasses

print("=== Publication Information ===")
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Python Programming Guide", "Guido van Rossum")

pub1.display_info()
print()
pub2.display_info()

print("\n=== Book Information ===")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Clean Code", "Robert C. Martin", 464)


print("Testing invalid page assignment on Book 1:")
book1.set_number_of_pages(-310) 

print("\nBook 1 Details:")
book1.display_info()

print("\nBook 2 Details:")
book2.display_info()

print("\n=== Magazine Information ===")
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("TIME Magazine", "Time USA, LLC", 50)


print("Testing invalid issue number assignment on Magazine 1:")
mag1.set_issue_number(0)

print("\nMagazine 1 Details:")
mag1.display_info()

print("\nMagazine 2 Details:")
mag2.display_info()
