from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {"id":0,
     "author":"mod",
     "language":"english",
     "title" : "anyiga adi"
    },
    {"id":1,
     "author":"anyi",
     "language":"igbo",
     "title":"yadiba"     
    },
    {"id":2,
     "author":"uwa_ezuoke",
     "language":"english",
     "title": "thats it"    
    },
    {"id":3,
     "author":"onyebuchi",
     "language":"hausa",
     "title":"jesus bu eze"     
    }
]

@app.route('/books', methods=['POST','GET'])
def books():
    #This retrieve the original data
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)

        else:
            "nothing found", 404


    #Adding of new data ta the database
    if request.method == 'POST':
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        ID = books_list[-1]["id"]+1

        new_obj = {"id":ID,
                    "author":new_author,
                    "language":new_lang,
                    "title":new_title     
    }

    books_list.append(new_obj)
    return jsonify(books_list), 201

@app.route('/books/<int:id>', methods = ["GET", "PUT", "DELETE"])
def single_book(id):
    if request.method == "GET":
        for book in books_list:
            if book["id"] == id:
                return jsonify(book)

    
    #updating the already existing data in the data base
    if request.method == 'PUT':
        for book in books_list:
            if book["id"] == id:
                book["author"] = request.form["author"]
                book["language"] = request.form["language"]
                book["title"] = request.form["title"]
                

                updated_book = {"id":id,
                            "author":book["author"],
                            "language":book["language"],
                            "title":book["title"]     
                            }

                return jsonify(updated_book)

    #Removing the data that have been existing in th database
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book["id"] == id:
                books_list.pop(index)
                return jsonify(books_list)

if __name__ == '__main__':
    app.run()