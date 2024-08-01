from tinyrpc.dispatch import public

@public
# {"id":1,"jsonrpc":"2.0","method":"getModel","params":{"resource":"StreamingService"}}
def getModel(resource):
    print("__name__")
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"itemAdded","params":{"resource":"ScenesService"}}
def itemAdded(resource):
    print("__name__")
    return ""