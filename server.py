from flask import Flask, render_template, redirect, request, session
import queries


app = Flask(__name__)


@app.route('/' , methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/mentors')
def mentors_list():
    columns = ["First name","Last name","School","Country"]
    db_columns = ["first_name","last_name","name","country"]
    data = queries.get_mentors()
    return render_template('list.html',data = data,columns = columns, db_columns=db_columns)

@app.route('/all-school')
def all_school():
    columns = ["First name","Last name","School","Country"]
    db_columns = ["first_name","last_name","name","country"]
    data = queries.all_school_list()
    return render_template('list.html',data = data,columns =columns , db_columns=db_columns)

@app.route('/mentors-by-country')
def mentors_by_country():
    columns = ["Country","Count"]
    data = queries.count_mentors()
    db_columns = ["country","count"]
    return render_template('list.html',data = data,columns =columns, db_columns=db_columns)

@app.route('/contacts')
def contacts():
    columns = ["School","First name","Last name"]
    data = queries.contacts()
    db_columns = ["name","first_name","last_name"]
    return render_template('list.html',data = data,columns =columns, db_columns=db_columns)

@app.route('/applicants')
def applicants():
    data = queries.applicants()
    columns = ["Application code","First name","Date"]
    db_columns = ["application_code","first_name","creation_date"]
    return render_template('list.html',data = data,columns =columns, db_columns=db_columns)

@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    data = queries.applicants_and_mentors()
    columns = ["Application code","First name","Mentor last name","Mentor first name"]
    db_columns = ["application_code","first_name","mentor_last","mentor_first"]
    return render_template('list.html',data = data,columns =columns, db_columns=db_columns)

if __name__ == "__main__":
    app.run(debug=True, port=5000)