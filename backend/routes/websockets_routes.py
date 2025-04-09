from flask_socketio import emit
from app import socketio
from app.models.virtual_model import VirtualModel
from app.models.QwenModel import QwenModel # type: ignore
llm = None

@socketio.on('message_1')
def handle_message_1(text):
    global llm
    if llm is None:
        emit('response',{'data':f'loading...'})
        llm = VirtualModel()
    print(f"输入: {text}")
    #virtual_model = VirtualModel()
    result = llm.infer(text)
    emit('response', {'data': f'服务器已收到: {result}'})

@socketio.on('message_2')
def handle_message_2(text):
    global llm
    if llm is None:
        emit('response',{'data':f'loading...'})
        llm = QwenModel()
    print(f"输入: {text}")
    #virtual_model = VirtualModel()
    result = llm.infer(text)
    emit('response', {'data': f'服务器已收到: {result}'})

@socketio.on('disconnect')
def handle_disconnect():
    global llm
    print('客户端断开连接')
    if llm:
        del llm
        llm = None
        print('已删除模型实例')
