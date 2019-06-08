import os 

from financemgr import logger 
from financemgr.db import engine, Base, Session   
from financemgr.config import DB_PATH
from financemgr.model import User, Account, Record



SAMPLE_USERS = {
    "user_1" : [{
        "name" : "Intro",
        "records" : [
            { "title" : "Pills", "value" : 50.0 },
            { "title" : "Watermelon", "value" : 6.0 },
            { "title" : "Wine", "value" : 20.0 }
        ]
    }],
    "user_2" : [
        {
            "name" : "Gold",
            "records" : [
                { "title" : "Wood", "value" : 3000.0 },
                { "title" : "Engine Oil", "value" : 2100.0 }
            ]
        },
        {
            "name" : "Personal",
            "records" : [
                { "title" : "Watch", "value" : 1200.0 }
            ]
        }
    ]
}

def init_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    Base.metadata.create_all(engine) 
    session = Session()
    for user, accounts in SAMPLE_USERS.items():
        user_ = User(name = user)
        for account in accounts:
            account_ = Account(name = account.get("name"))
            for record in account["records"]:
                account_.records.append(
                    Record(
                        record_title = record.get("title", ""),
                        record_value = record.get("value", 0.0)
                    )
                )
            logger.info("User: {} Account added -- {}".format(user, account["name"]))
            user_.accounts.append(
                account_
            )
        logger.info("User added -- {}".format(user))
        session.add(user_)
    session.commit()

if __name__ == "__main__":
    init_db()
    session = Session()
    for user in session.query(User).filter(User.name == "user_1"):
        print(user.name)
        print(" --- ")
        print("Accounts count: {}".format(len(user.accounts)))

