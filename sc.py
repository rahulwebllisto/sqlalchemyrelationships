from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base,sessionmaker ,relationship
from sqlalchemy import Column, Integer, String ,ForeignKey,Table
engine = create_engine('sqlite:///mynew.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

###one to many relationship
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    product = relationship('Product',backref='customer')
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer,primary_key= True)
    pname = Column(String)
    user_id = Column(Integer,ForeignKey('user.id'))
    def __repr__(self):
        return "<Product(pname='%s')>"%(self.pname)


#one to one
##for one to one relationship set uselist=False
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    bag = relationship('Bag',backref='student',uselist=False)
    def __repr__(self):
        return "<Student(name='%s')>"%(self.name)


class Bag(Base):
    __tablename__ = 'bag'
    id = Column(Integer,primary_key=True)
    name= Column(String)
    student_id = Column(Integer,ForeignKey(Student.id))
    def __repr__(self):
        return "<Bag(name='%s')>"%(self.name)


#many to many relationship

association_table = Table(
    'association',
    Base.metadata,
    Column('developer_id',ForeignKey('developer.id')),
    Column('project_id',ForeignKey('project.id'))

)

class Developer(Base):
    __tablename__= 'developer'
    id = Column(Integer,primary_key=True)
    dev = Column(String)
    projects = relationship('Project',secondary=association_table,
    back_populates='developers'
    )

    def __repr__(self):
        return "<Developer(dev='%s')>"%(self.dev)

class Project(Base):
    __tablename__= 'project'
    id = Column(Integer,primary_key=True)
    proj = Column(String)
    developers = relationship('Developer',secondary=association_table,
    back_populates='projects'
    
    )

    def __repr__(self):
        return "<project(proj='%s')>"%(self.proj)

# Base.metadata.create_all(engine)
# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# session.add(ed_user)
# print(ed_user.nickname)
# session.commit()
# local_session = Session(bind=engine)
# n =local_session.query(User.product).all()
# print(n)
# u =session.query(User).filter(User.id==1).first()
# print(u.product)

s = session.query(Project).filter(Project.id==3).first()
print(s.developers)