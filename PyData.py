from flask import Flask, render_template
from flask_restful import Resource, Api
import psutil
from psutil._common import bytes2human
app = Flask(__name__)
api = Api(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/etc/')
def etc():
    return render_template('etc.html')

@app.route('/todo/')
def todo():
    return render_template('todo.html')

@app.route('/stat/')
def stat():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    system_info_data = {
        'cpu_percent': psutil.cpu_percent(interval=1, percpu=True),

        'cpu_mem_total': memory.total,
        'cpu_mem_used': memory.used,
        'cpu_mem_percent': memory.percent,

        'disk_usage_total': disk.total,
        'disk_usage_used': disk.used,
        # "disk_usage_human": bytes2human(disk.used),
        'disk_usage_percent': disk.percent,

        'sensor_temperatures': psutil.sensors_temperatures().get("cpu_thermal")[0][1]}
    
    return render_template('stat.html', var = system_info_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
