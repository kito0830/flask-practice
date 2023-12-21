from models import db, Employee, Project, Company, app

# create
john = Employee('John')
adam = Employee('Adam')

# add employee
with app.app_context():
  db.session.add_all([john, adam])
  db.session.commit()
  
  # create company
  company1 = Company('Company1', john.id) #employee_id = john.id
  company2 = Company('Company2', adam.id) #employee_id = adam.id

# # add company
with app.app_context():
  db.session.add_all([company1, company2])
  db.session.commit()
  
# # create project
john_project1 = Project('Project1', john.id) #employee_id = john.id
john_project2 = Project('Project2', john.id) #employee_id = john.id
adam_project1 = Project('Project3', adam.id) #employee_id = adam.id
adam_project2 = Project('Project4', adam.id) #employee_id = adam.id

with app.app_context():
  db.session.add_all([john_project1, john_project2, adam_project1, adam_project2])
  db.session.commit()