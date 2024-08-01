from socket import AF_INET, SOCK_STREAM, socket
from tinyrpc.dispatch import RPCDispatcher
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from methods import collections_methods, scenes_methods, sources_methods, fouretout_methods

# Add all methods to Dispatcher
dispatcher = RPCDispatcher()

dispatcher.add_method(collections_methods.collectionRemoved)
dispatcher.add_method(collections_methods.collectionSwitched)
dispatcher.add_method(collections_methods.collectionUpdated)

dispatcher.add_method(scenes_methods.activeScene)
dispatcher.add_method(scenes_methods.getScenes)
dispatcher.add_method(scenes_methods.sceneAdded)
dispatcher.add_method(scenes_methods.sceneRemoved)

dispatcher.add_method(sources_methods.getSourcesForCurrentScene)
dispatcher.add_method(sources_methods.sourceAdded)
dispatcher.add_method(sources_methods.sourceRemoved)

dispatcher.add_method(fouretout_methods.getModel)
dispatcher.add_method(fouretout_methods.itemAdded)

rpc = JSONRPCProtocol()

# Server
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('127.0.0.1', 28194))
sock.listen(5)
while True:
    connection,address = sock.accept()
    buf = connection.recv(8000)
    if buf != b'':
        #print(buf)
        rpc_request = rpc.parse_request(buf)
        print(f'{rpc_request.unique_id} - {rpc_request.method} - {rpc_request.args} {rpc_request.kwargs}')
        #print(dispatcher.dispatch(rpc_request).serialize())
        #connection.send(dispatcher.dispatch(rpc_request).serialize())
    connection.close()