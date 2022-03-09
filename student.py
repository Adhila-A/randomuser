import names
import  random
import datetime
from flask import Flask, jsonify, render_template
app=Flask(__name__,template_folder='template') 
@app.route("/")
def check():
    Student_dict=[]
    for i in range(5):
                    a=(names.get_first_name())
                    b=(names.get_last_name())
                    fullname=(a+" "+b)
                    emailid=a+b+"@gmail.com"
                    ID=i+1
                    random_number = random.randint(9000000000, 10000000000)
                    salary=random.randrange(25000,75000,100)
                    start_date = datetime.date(2000, 1, 1)
                    end_date = datetime.date(2022, 1, 1)
                    time_between_dates = end_date - start_date
                    days_between_dates = time_between_dates.days
                    random_number_of_days = random.randrange(days_between_dates)
                    random_date = start_date + datetime.timedelta(days=random_number_of_days)
                    experience=end_date.year-random_date.year
                    profession=["Web Developer ","Physician",  "Auditor" ,"Health Educator"  ,"RestaurantManager" ,
                    "Executive Director"  ,"Front Desk Coordinator" ,"Clerk" "Paramedic", "IT Support Staff",
                    "Laboratory Technician", "Software Engineer", "Webmaster" ,"Business Broker" ,"Software  Developer",  "Mobile Developer"]
                    Prof=(random.choice(profession))
                    Student_dict+=[{"ID":ID,'NAME':fullname,'EMAIL': emailid ,'PHONENUMBER':random_number ,
                    'PROFESSION':Prof,'SALARY':salary ,'DATE_OF_JOINING':random_date,'YEAR_OF_EXPERIENCE':experience}]
                    print(Student_dict)
                    student_details=jsonify(Student_dict)

    return render_template("student.html",data=student_details)

if(__name__)=="__main__":
     app.run(debug=True)
