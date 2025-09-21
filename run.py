from src.main import Main

if __name__ == '__main__':
    main = Main("*")
    main.socketio.run(main.app, host='localhost', port=4500, debug=True)