def individual_employee(employee):
    return{
        "id": employee['id'],
        "name": employee['name'],
        "age": employee['age'],
        "department": employee['department'],
        "salary": employee['salary']
    }

def all_employees(employees):
    return [individual_employee(employee) for employee in employees]