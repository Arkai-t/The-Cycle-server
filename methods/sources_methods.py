from tinyrpc.dispatch import public

@public
# {"id":1,"jsonrpc":"2.0","method":"getSourcesForCurrentScene","params":{"resource":"AudioService"}}
def getSourcesForCurrentScene(resource):
    return ""

@public
#{"id":200,"jsonrpc":"2.0","method":"sourceAdded","params":{"resource":"SourcesService"}}
def sourceAdded(resource):
    return ""

@public
# {"id":1,"jsonrpc":"2.0","method":"sourceRemoved","params":{"resource":"SourcesService"}}
def sourceRemoved(resource):
    return ""

@public
#1 - sourceUpdated - [] {'resource': 'SourcesService'}
def sourceUpdated(resource):
    return ''