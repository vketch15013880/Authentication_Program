print("Login Authentication Program")
''' 
Dictionary

1. Menu opens
2. Welcome title
3. Offer user options
    i. Login (existing user)
        - 
    ii. Create Account 
'''

class TextPage: 
    def __init__(self): 
        self._components: dict = {}
    
    @property
    def components(self) -> dict:
        return self._components
    
    @property
    def componentNames(self) -> list:
        return list(self.components.keys())
    
    @property
    def getContent(self, componentName: str) -> str:
        """
        For adding & changing TextPage object components 
        """
        return self.components[componentName]

    def titleFormat(self, content: str):
        """
        Returns the content of a TextPage object component in title format 
        """
        dashCount = len(content) + 4
        top = '+' + ('-' * dashCount) + '+'
        middle = '\n|' + f"  {content}  " + "|\n"
        bottom = top
        formattedTitle = top + middle + bottom
        return formattedTitle
        
    def update(self, componentName: str, content: str, newlineAmount: int = 0, isTitle: bool = False):
        """
        For adding & changing components of a TextPage object.
        If a component with the current 'componentName' argument already exists, its content
        will be overwritten by the current 'content' argument.
        """
        if (isTitle):
            content = self.titleFormat(content)
        self.components.update({componentName: (content + ('\n' * newlineAmount))})

    def remove(self, componentName: str):
        """
        For removing components of a TextPage object 
        """
        del self.components[componentName]
    
    def __str__(self):
        return ''.join(list(self.components.values()))

    
'''
Class for user interactivity
'''
'''
Class for storing username/password pairs
    - can also store temporary username/password for when user
      is creating a login
'''

if __name__ == "__main__":
    MenuPage = TextPage()
    MenuPage.update("welcomeMsg", "Welcome to the Login Authentication Program", 2, True)
    MenuPage.update("exitMsg", "# at any time, enter 'menu' to return to the menu page")
    print(MenuPage)
    print("-" * 9)
    print("woo" + ('yes' * 10))


i = 5
i = "changed"

myDictionary = {"ok": 5}
myDictionary = 10