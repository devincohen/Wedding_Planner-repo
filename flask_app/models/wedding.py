from flask_app.config.mysqlconnection import connectToMySQL

class Wedding:
    def __init__(self, data):
        self.id = data["id"]
        self.guest_list = data["guest_list"]
        self.gift_list = data["gift_list"]
        self.partner1 = data["partner1"]
        self.partner2 = data["partner2"]
        self.location = data["location"]
        self.reception = data["receptions"]
        self.notes = data["notes"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
        # date
        # guest list
        # gift list
        # partner1
        # partner 2
        # location
        # reception - can potentially be a whole other planning center ordeal, but 
        #   maybe we stick with a dictionary: address, time, kids_allowed
        # notes
        # user_id because a wedding cant exist without a user

    @classmethod
    def save(cls, data):
        query = """INSERT INTO  --database--(guest_list, gift_list, partner1, partner2, location, reception, notes, created_at, updated_at) 
                VALUES (%(guest_list)s, %(gift_list)s, %(partner1)s, %(partner2)s, %(location)s, %(reception)s, %(notes)s, NOW(), NOW())
            """
        return connectToMySQL("--database--").query_db(query, data)
    
    @classmethod
    def get_all_for_user(cls, user_id):
        query = """SELECT * from weddings 
                WHERE user_id = %(user_id)s """
        data = {"id" : user_id}
        result = connectToMySQL("--database--").query_db(query, data)
        return cls(result)
        

    @classmethod
    def get_one(cls, wedding_id):
        query = """SELECT * from weddings 
        WHERE id = %(wedding_id)s
            """
        data = {"id" : wedding_id}
        result = connectToMySQL("--database--").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE weddings
                SET guest_list=%(guest_list)s   gift_list=%(gift_list)s   partner1=%(partner1)s     partner2=%(partner2)s    location=%(location)s     reception=%(reception)s    notes=%(notes)s 
            """
        return connectToMySQL("--database--").query_db(query, data)
    
    @classmethod
    def delete(cls, wedding_id):
        query = """DELETE from weddings 
                WHERE id = %(wedding_id)s """
        data = {"id" : wedding_id}
        return connectToMySQL("--database--").query_db(query, data)