from financemgr.root import RootWindow
from financemgr.ui import SelectUser 
from financemgr.ui import UserUi 

class AppController():
    def __init__(self):
        self.db = Session()
        self.root = RootWindow(self)
        self.frames = self.root.init_frames((SelectUser, UserUi))
        self.current_frame = None 
        self.change_ui("SelectUser")
        self.current_user = None 

    def get_users(self):
        users = self.db.query(User).all()    
        return [ user.name for user in users ]    
    
    def get_accounts_for_user(self, user_id):
        pass 
    
    def get_records_for_user(self, *accounts):
        pass 

    def open_user_by_name(self, name):
        user = self.db.query(User).filter(User.name == name).first()
        self.current_user = user 
        self.change_ui("UserUi")

    def load_current_user(self, name):
        """ Loads current user from controller into frame"""
        assert self.current_user is not None, "Current User cannot be None"

        

    def change_ui(self, name):
        if name in self.frames:
            if self.current_frame != None:
                self.frames[self.current_frame].on_exit_frame_hook()
            self.current_frame = name 
            self.root.show_frame(name)
            self.frames[self.current_frame].on_enter_frame_hook()   
        