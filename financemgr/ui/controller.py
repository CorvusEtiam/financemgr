from .root import RootWindow
from .user_select import SelectUser 
from financemgr import Session
from financemgr.model import User

class AppController():
    def __init__(self):
        self.db = Session()
        self.root = RootWindow(controller = self)
        self.frames = self.root.init_frames([SelectUser]) #, CurrentUser))
        self.current_frame = None 
        self.current_user = None 
        
        self.change_ui("SelectUser")

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
        self.change_ui("CurrentUser")

    def load_current_user(self, name):
        """ Loads current user from controller into frame"""
        assert self.current_user is not None, "Current User cannot be None"

    def run(self):
        self.root.mainloop()

    def change_ui(self, name):
        if name in self.frames:
            if self.current_frame != None:
                self.frames[self.current_frame].on_exit_frame_hook()
            self.current_frame = name 
            frame = self.root.show_frame(name)
            frame.on_enter_frame_hook()
        else:
            raise Exception(f"No UI frame with name: {name} found")
