from flask import render_template, redirect, url_for, request
from app import app

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/start_service', methods=['POST'])
def start_service():
    # return redirect(url_for('websocket_page'))
    model_type = request.form.get('model_type')
    # model_type = request.get['model.type']
    if model_type == 'model1':
        return redirect(url_for('websocket_page'))
    elif model_type == 'model2':
        return redirect(url_for('websocket_page2'))

"""
@app.route('/websocket')
def websocket_page():
    return render_template('index.html')
"""

@app.route('/websocket/model1')
def websocket_page():
    return render_template('index_model1.html')

@app.route('/websocket/model2')
def websocket_page2():
    return render_template('index_model2.html')
