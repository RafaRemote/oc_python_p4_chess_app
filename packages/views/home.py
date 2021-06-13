from packages.controllers.menu import MenuController
# from packages.controllers.welcome import WelcomeController



class HomeMenu:
    def __init__(self):
        self.name = self.__class__.__name__
        # self.name = 'bob'

    def __call__(self):
        # welcome = WelcomeController()
        # welcome()

        menu = MenuController(self.name, choice=None)
        menu()    

        


    
  

        
        
        

    


