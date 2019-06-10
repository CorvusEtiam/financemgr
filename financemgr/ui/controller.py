from .root import RootWindow
from financemgr import Session

from financemgr.model import User
from .user_select import SelectUser 
from .user_account import CurrentUser 
from .user_edit import EditUser 

class AppController():
    def __init__(self):
        self.db = Session()
        self.root = RootWindow(controller = self)
        self.frames = self.root.init_frames([SelectUser, CurrentUser, EditUser]) #, CurrentUser))
        self.current_frame = None 
        self.current_user = None 
        
        self.change_ui("SelectUser")

    def get_users(self):
        """List of usernames as [str]
            :returns: list[str]
        """
        users = self.db.query(User).all()    
        return [ user.name for user in users ]    
    
    def get_accounts_for_user(self, user_id):
        pass 
    
    def get_records_for_user(self, *accounts):
        pass 

    def get_user_by_name(self, name):
        user = self.db.query(User).filter(User.name == name).first()
        return user 
    
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

