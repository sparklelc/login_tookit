# -*- coding: utf-8 -*-

from login_agent import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
