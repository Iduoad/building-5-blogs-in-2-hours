from flask import jsonify, request, abort
import flask_cors

from blog import app, db
from blog.models import Post


def check_request_json(request, required_fields = []):
    if not request.json:
        return False

    for rf in required_fields:
        if rf not in request.json:
            return False

    return True

def create_post_from_request(request):
    new_post = Post(title= request.json['title'], content=request.json['content'])
    db.session.add(new_post)
    db.session.commit()

    return { 'status' : 'success' }

def get_post_from_request(request):
    post_id = int(request.args['id'])
    return Post.query.filter_by(id=post_id).first()

def update_post_from_request(request):
    post_id = int(request.json['id'])
    post = Post.query.filter_by(id=post_id).first()

    post.title = request.json['title']
    post.content = request.json['content']

    db.session.commit()

    return { 'status' : 'success' }

def delete_post_from_request(request):
    post_id = int(request.json['id'])
    post = Post.query.filter_by(id=post_id).first()

    db.session.delete(post)
    db.session.commit()

    return { 'status' : 'success' }


@app.route('/posts/')
def get_all_posts():
    posts = Post.query.order_by(-Post.created_on).all()
    posts_json = [i.serialize() for i in posts]

    return jsonify({ 'posts' : posts_json })

# @app.route('/post/<int:post_id>')
# def get_post(post_id):
#     post = post.query.filter_by(id=post_id).first()
#     return jsonify(post.serialize())

@app.route('/post', methods=['GET', 'POST', 'PUT', 'DELETE'])
def post_ressource():
    if request.method == 'GET':
        if 'id' not in request.args:
            abort(404)

        post = get_post_from_request(request)
        return jsonify({'post': post.serialize()}), 200

    elif request.method == 'POST':
        check_request_json(request, ['title', 'content']) or abort(404)
        response_json = create_post_from_request(request)
        return jsonify(response_json), 201

    elif request.method == 'PUT':
        check_request_json(request, ['id', 'title', 'content']) or abort(404)
        response_json = update_post_from_request(request)
        return response_json, 201

    elif request.method == 'DELETE':
        check_request_json(request, ['id']) or abort(404)
        response_json = delete_post_from_request(request)
        return jsonify(response_json), 200

if __name__ == '__main__':
    app.run(debug=True)
