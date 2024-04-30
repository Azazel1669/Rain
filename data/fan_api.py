import flask
from flask import jsonify, make_response, request

from . import db_session
from .fan import Fan
from random import randint

HOST = '127.0.0.1'
PORT = '8080'
blueprint = flask.Blueprint(
    'fan_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/fan')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Fan).all()
    return jsonify(
        {
            'fan':
                [item.to_dict(only=('title', 'content', 'fandom', 'user.name'))
                 for item in news]
        }
    )


@blueprint.route('/api/fan', methods=['POST'])
def create_news():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['title', 'content', 'fandom', 'user_id']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    fan = Fan(
        title=request.json['title'],
        content=request.json['content'],
        fandom=request.json['fandom'],
        user_id=request.json['user_id']
    )
    db_sess.add(fan)
    db_sess.commit()
    return jsonify({'id': fan.id})


@blueprint.route('/api/fan/<int:fan_id>', methods=['GET'])
def get_one_news(fan_id):
    db_sess = db_session.create_session()
    fan = db_sess.query(Fan).get(fan_id)
    if not fan:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'fan': fan.to_dict(only=(
                'title', 'content', 'fandom', 'user_id'))
        }
    )


@blueprint.route('/api/random', methods=['GET'])
def get_random():
    db_sess = db_session.create_session()
    news = db_sess.query(Fan).all()
    random_id = news[randint(1, len(news)) - 1].id
    link = f'https://literate-exultant-joke.glitch.me/book/{random_id}' 
    return jsonify({'link': link})
