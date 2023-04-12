import csv
from string import Template 

with open("./data.ddl","w") as output:
    with open("./item.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO item VALUES ($item_no,$price,$quantity,$description);\n').safe_substitute(item_no=row[0],price=row[1],quantity=row[2],description='"'+(row[3])+'"'))

    with open("./cashier.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO cashier VALUES ($id,$name);\n').safe_substitute(id=row[0],name='"'+row[1]+'"'))

    with open("./bill.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO bill VALUES ($bill_no,$total_cost,$tax,$total_amount,$order_details);\n').safe_substitute(bill_no=row[0],total_cost=row[1],tax=row[2],total_amount='"'+(row[3])+'"',order_details='"'+(row[4])+'"'))

    with open("./delivery_person.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO delivery_person VALUES ($id,$name);\n').safe_substitute(id=row[0],name='"'+(row[1])+'"'))

    with open("./customer.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO customer VALUES ($name,$phone,$address);\n').safe_substitute(name='"'+(row[0])+'"',phone='"'+(row[1])+'"',address='"'+(row[2])+'"'))

    with open("./waiter.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO waiter VALUES ($waiter_id,$name);\n').safe_substitute(waiter_id=row[0],name='"'+(row[1])+'"'))

    with open("./chef.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO chef VALUES ($chef_id,$name);\n').safe_substitute(chef_id=row[0],name='"'+(row[1])+'"'))
 
    with open("./order.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO order VALUES ($order_no,$order_date,$price,$order_type);\n').safe_substitute(order_no=row[0],order_date='"'+(row[1])+'"',price=row[2],order_type='"'+(row[3])+'"'))
 
    with open("./manager.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO manager VALUES ($id,$contact,$name);\n').safe_substitute(id=row[0],contact=row[1],name='"'+(row[2])+'"'))
    
    with open("./paid_to.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO paid_to VALUES ($cashier_id,$bill_no);\n').safe_substitute(cashier_id=row[0],bill_no=row[1]))
  
    with open("./pays.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO pays VALUES ($bill_no,$phone);\n').safe_substitute(bill_no=row[0],phone='"'+row[1]+'"'))


    with open("./places.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO places VALUES ($phone,$order_no);\n').safe_substitute(phone='"'+row[0]+'"',order_no=row[1]))


    with open("./assigned_delivery.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO assigned_delivery VALUES ($phone,$delivery_person_id);\n').safe_substitute(phone='"'+row[0]+'"',delivery_person_id=row[1]))


    with open("./assigned_waiter.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO assigned_waiter VALUES ($phone,$waiter_id);\n').safe_substitute(phone='"'+row[0]+'"',waiter_id=row[1]))


    with open("./taken_by.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO taken_by VALUES ($waiter_id,$order_no);\n').safe_substitute(waiter_id=row[0],order_no=row[1]))


    with open("./contains.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO contains VALUES ($item_no,$order_no);\n').safe_substitute(item_no=row[0],order_no=row[1]))


    with open("./prepare.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO prepare VALUES ($chef_id,$order_no);\n').safe_substitute(chef_id=row[0],order_no=row[1]))


    with open("./manager.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        field=next(csvreader)
        for row in csvreader:
            output.write(Template('INSERT INTO manager VALUES ($id,$contact,$name);\n').safe_substitute(id=row[0],contact=row[1],name='"'+(row[2])+'"'))