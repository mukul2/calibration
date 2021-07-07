from flask import Flask
from flask import Flask, jsonify, request
import numpy as np
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/calibration', methods=['GET', 'POST','DELETE', 'PATCH'])
def calirbation():
    # json_data = request.get_json(force=True)
    # un = json_data['username']
    # pw = json_data['password']
    content = request.json
    #xAxis = content['x']
    #yAxis = content['y']
   # x = [5, 10, 20.01, 30, 40, 50.01, 60.02]
   # y = [274046, 523207, 1015404, 1494790, 1978860, 2461945, 2951055]
    x =  content['x']
    y =  content['y']
    d = content['d']
    print(np.polyfit(y, x, 3))
    print('%.20f' % np.polyfit(y, x, 3)[0])
    print('%.20f' % np.polyfit(y, x, 3)[1])
    print('%.20f' % np.polyfit(y, x, 3)[2])
    print('%.20f' % np.polyfit(y, x, 3)[3])
    fit = np.polyfit(y, x, 3)


    return {"1":'%.20f' % fit[0],"2":'%.20f' % fit[1],"3":'%.20f' % fit[2],"4":'%.20f' % fit[3],}
if __name__ == '__main__':
    app.run()
