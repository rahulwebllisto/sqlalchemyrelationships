from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base,sessionmaker ,relationship
from sqlalchemy import Column, Integer, String ,ForeignKey,Table
engine = create_engine('sqlite:///joinsql.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    name = Column(String(50))

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'))
    name = Column(String(50))
    salary = Column(Integer)

results = session.query(Employee, Department).join(Department).all()

for employee, department in results:
    print(employee.name, department.name)

# results = session.query(Employee, Department, Company). \
#     select_from(Employee).join(Department).join(Company).all()

# for employee, department, company in results:
#     print(employee.name, department.name, company.name)

# results = session.query(Employee.name, Employee.salary).join(Department).join(Company). \
#     filter(Department.id == 1).all()

# for result in results:
#     print(result)
# Base.metadata.create_all(engine)