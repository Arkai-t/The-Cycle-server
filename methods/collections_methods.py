from tinyrpc.dispatch import public

@public
# {"id":1,"jsonrpc":"2.0","method":"collectionAdded","params":{"resource":"SceneCollectionsService"}}
def collectionAdded(resource):
    print("__name__")
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"collectionRemoved","params":{"resource":"SceneCollectionsService"}}
def collectionRemoved(resource):
    print("__name__")
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"collectionSwitched","params":{"resource":"SceneCollectionsService"}}
def collectionSwitched(resource):
    print("__name__")
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"collectionUpdated","params":{"resource":"SceneCollectionsService"}}
def collectionUpdated(resource):
    print("__name__")
    return ""