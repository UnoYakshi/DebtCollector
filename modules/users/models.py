#!/modules/users/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Date
#from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class User(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    birthday = Column(Date)
    #personal_phone = Column(String(20))
    #personal_cellphone = Column(String(20))
    #contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
    #contact_group = relationship("ContactGroup")

    def __repr__(self):
        return [self.id, self.first_name, self.last_name]
