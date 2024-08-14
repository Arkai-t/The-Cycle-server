from tinyrpc.dispatch import public

@public
# {"id":1,"jsonrpc":"2.0","method":"getModel","params":{"resource":"StreamingService"}}
def getModel(resource):
    return ''

@public
#1 - studioModeChanged - [] {'resource': 'TransitionsService'}
def studioModeChanged(resource):
    return ''

@public
#1 - state - [] {'resource': 'TransitionsService'}
def state(resource):
    return ''

@public
#1 - streamingStatusChange - [] {'resource': 'StreamingService'}
def streamingStatusChange(resource):
    return ''
