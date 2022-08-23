from flask import Flask, render_template, redirect, request

app = Flask('app')

todos = []

@app.route('/')
def index():
  return render_template('index.html', todos = todos)

@app.route('/store', methods=['POST'])
def creat():
  casa = request.form.get('casa')
  gol = request.form.get('gol1')
  visitante = request.form.get('visitante')
  gol2 = request.form.get('gol2')
  todos.append ({
    'title': casa,
    'gol1': gol,
    'title2': visitante,
    'gol2': gol2
  })
  return redirect('/')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)