import csv
import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/publication', methods=['GET', 'POST'])
def publication():
    if request.method == 'POST':
        # Domain = request.form['Domain']
        Authors = request.form['Authors']
        Years = request.form['Years']
        Ptype = request.form['Ptype']

        # mylist = [[Ptype, Authors, Years]]
        # mylist1 = [Ptype, Authors, Years]
        # if Ptype == 'Journal':
        #     with open('Common_publication1.csv', mode='r') as f:
        #         reader = csv.reader(f)
        #     # # reader.readrow(mylist)
        #     # for row in reader:
        #     #     print(row)
        #     return render_template('new.html', tables=[f.to_html()], titles=[''])

        # elif request.method == 'GET':
        #     return 'A GET request was made'
        # else:
        #     return 'Not a valid request method for this route'
        if Ptype == 'Journal':
            data1 = pd.read_csv('Common_publication1.csv', index_col=0)
            # x = data['Title']
            x1 = pd.DataFrame(data1)
            x2 = x1['Year'] == Years
            x1.where(x2)
            return render_template('new.html', tables=[x1.to_html()], titles=[''])
        elif Ptype == 'Book':
            data2 = pd.read_csv('books_new.csv', index_col=0)
            # x = data['Title']
           # y1 = pd.DataFrame(data2)
            y1 = data2['Faculty_author'] == request.form['Authors']
            data01 = data2.where(y1)
        #    # return render_template('new.html', Years=request.form['Years'])
            return render_template('new.html', tables=[data01.to_html()], titles=[''])

            # if data2['Year'] == request.form['Years']:
            #   return render_template('new.html', tables=[data2.to_html()], titles=[''])

        else:
            data3 = pd.read_csv('conference.csv', index_col=0)
            # x = data['Title']
            z1 = pd.DataFrame(data3)
            return render_template('new.html', tables=[z1.to_html()], titles=[''])


#         file1 = open(Common publication.csv, 'rb')
# reader = csv.reader(file1)
# new_rows_list = []
# for row in reader:
#    if row[2] == 'Test':
#       new_row = [row[0], row[1], 'Somevalue']
#       new_rows_list.append(new_row)
#       file1.close()


# return render_template('publication_d.html',title=request.form['Title'],name=request.form['Author'])
if __name__ == "__main__":
    app.run(debug=True)
