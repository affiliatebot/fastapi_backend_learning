# models/subscribers.py
from sqlalchemy import Column, Integer,DateTime, ForeignKey, UniqueConstraint
from database.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Subscriber(Base):

    __tablename__ = "subscribers" 

    id = Column(Integer,primary_key=True,index=True)
    creator_id = Column(Integer,ForeignKey("user.id"),index=True,nullable=False)
    subscriber_id = Column(Integer,ForeignKey("user.id"),index=True,nullable=False)

    # to sort followers by time
    created_at = Column(DateTime,default=func.now(),nullable=False)
    
    # to store history and refollow logic
    delete_at = Column(DateTime, default=False,nullable=False)

    # rule to prevent duplicate follows
    __table_args__ = (
        UniqueConstraint("subscriber_id", "creator_id", name="unique_subscribers"),
    )
    # orm relationships
     
    # sub = Subscription(
    #                     subscriber_id = userA.id,
    #                     creator_id = userB.id
    #                   )
    
    
    
    # sub.subscriber = userA → userA.following updated

    subscriber = relationship("User",
                              foreign_keys=[subscriber_id],
                              back_populates="following")
    
    # sub.creator = userB  → userB.followers updated
    creator = relationship("User",
                              foreign_keys=[creator_id],
                              back_populates="followers")
    

