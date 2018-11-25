import pickle


options = {'1': 'ctrl+v', '2': 'enter', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', }
ip = ''
port = 12345
socket_flag = 0
conn_stat = True


def _pickling():
    global options
    global ip
    global port
    data = [options, ip, port]
    with open('Settings.pkl', 'wb') as f:
        pickle.dump(data, f)


def _unpickling():
    global options
    global ip
    global port
    try:
        with open('Settings.pkl', 'rb') as f:
            data = pickle.load(f)
        options = data[0]
        ip = data[1]
        port = data[2]
    except pickle.UnpicklingError as e:
        return()
    except FileNotFoundError as e:
        return()
