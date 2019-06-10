from financemgr.db import Session 
from financemgr.model import User 

from financemgr.ui.root import RootWindow 
from financemgr.ui.user_edit import EditUser
from financemgr.ui.user_select import SelectUser 
from financemgr.ui.user_view import CurrentUser 


class AppController():
    def __init__(self):
        self.db = Session()
        self.root = RootWindow(controller = self)
        self.frames = self.root.init_frames([SelectUser, CurrentUser, EditUser]) #, CurrentUser))
        self.current_frame = None 
        self.current_user = None 
        
        self.change_ui(SelectUser)

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

    @property
    def current_frame(self):
        return self.root.top_frame

    def change_ui(self, name_or_cls):
        if type(name_or_cls) is type:
            name = name_or_cls.__name__
        else:
            name = name_or_cls

        if name in self.frames:
            if self.current_frame != None:
                self.frames[self.current_frame].on_exit_frame_hook()
            frame = self.root.show_frame(name)
            frame.on_enter_frame_hook()
            self.root.push_frame(name)
        else:
            raise Exception(f"No UI frame with name: {name} found")

    def previous_ui(self):   
        current = self.root.pop_frame()
        self.frames[current].on_exit_frame_hook()
        self.frames[self.current_frame].on_enter_frame_hook()

    

