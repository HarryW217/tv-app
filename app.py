from flask import Flask, request, jsonify

app = Flask(__name__)

tv_show_list = [
    {
        "id": 0,
        "name": "Doctor Who",
        "genre": "Science Fiction" 
    },
    {
        "id": 1,
        "name": "Sherlock",
        "genre": "Crime" 
    },
    {
        "id": 2,
        "name": "Supernatural",
        "genre": "Fantasy" 
    },
    {
        "id": 3,
        "name": "Hannibal",
        "genre": "Crime" 
    },
    {
        "id": 4,
        "name": "Scooby-Doo! Where Are You?",
        "genre": "Animation" 
    },
]

@app.route('/shows', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(tv_show_list) > 0:
            return jsonify(tv_show_list)
        else:
            'Nothing Found', 404
            
    if request.method == 'POST':
        new_name = request.form['name']
        new_genre = request.form['genre']
        iD = tv_show_list[-1]['id']+1
        
        new_obj = {
            'id': iD,
            'name': new_name,
            'genre': new_genre
        }
        
        tv_show_list.append(new_obj)
        return jsonify(new_obj), 201
    
@app.route('/shows/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for show in tv_show_list:
            if show['id'] == id:
                return jsonify(show)
            pass
    if request.method == 'PUT':
        for show in tv_show_list:
            if show["id"] == id:
                show['name'] = request.form['name']
                show['genre'] = request.form['genre']
                updated_show = {
                    'id': id,
                    'name': show['name'],
                    'genre': show['genre']
                } 
                return jsonify(updated_show)
    if request.method == 'DELETE':
        for index, show in enumerate(tv_show_list):
            if show['id'] == id:
                tv_show_list.pop(index)
                return jsonify(tv_show_list)
    
if __name__ == '__main__':
    app.run()