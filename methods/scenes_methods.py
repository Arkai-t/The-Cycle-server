from tinyrpc.dispatch import public

@public
# {"id":1,"jsonrpc":"2.0","method":"getScenes","params":{"resource":"ScenesService"}}
def getScenes(resource):
    print("__name__")
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"sceneAdded","params":{"resource":"ScenesService"}}
def sceneAdded(resource):
    
    print("__name__")
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"sceneRemoved","params":{"resource":"ScenesService"}}
def sceneRemoved(resource):
    
    print("__name__")
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"activeScene","params":{"resource":"ScenesService"}}
def activeScene(resource):
    print("__name__")
    return ""
