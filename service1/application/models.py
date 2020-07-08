from application import db

class Users(db.Model):
      
   #  @login_manager.user_loader
    # def load_user(id):
      #   return Users.query.get(int(id))

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    rapper_name = db.Column(db.String(500), nullable=False)

    #def __repr__(self):
     #   return ''.join([
      #      'User ID: ', str(self.id), '\r\n',
       #     'Rapper_namel: ', self.rapper_name, '\r\n',
        #    'Name: ', self.first_name, ' ', self.last_name
       # ])
