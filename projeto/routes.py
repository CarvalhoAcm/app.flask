from projeto import app, db
from flask import render_template, request, redirect, url_for
from projeto.lista_filmes import resultado_filme
from projeto.livro import livro

conteudos  =  []
registros = []
@app.route('/', methods= ['GET', 'POST'])
def principal():
    if request.method == "POST":
        if request.form.get("conteudo"):
            conteudos.append(request.form.get("conteudo"))
    
    return render_template("index.html",
    conteudos=conteudos
                           
                           )

@app.route('/diario', methods=['GET', 'POST'])
def diario():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno')
            nota = request.form.get('nota')
            registros.append({
                "aluno":aluno,
                "nota":nota
            })
        
    return render_template('sobre.html',
    registros=registros)


@app.route('/filmes/<propriedade>')
def lista_filmes(propriedade):
    return render_template(
        "filmes.html",
        filmes= resultado_filme(propriedade)
        
    )
    
'''@app.route('/livro')
def lista_livro():
   return render_template('livro.html', livros=livro.query.all())'''

@app.route('/livro')
def lista_livro():
    page = request.args.get('page', 1, type=int)
    per_page = 2
    todos_livros = livro.query.paginate(page=page, per_page=per_page)
    return render_template("livro.html",
    livros = todos_livros)
    
@app.route('/add_livro', methods=["GET", "POST"])
def adiciona_livro():
    name = request.form.get('nome')
    descrição = request.form.get('descrição')
    valor = request.form.get('valor')
    if request.method == 'POST':
        add_livro = livro(
            name,
            descrição,
            valor
        )
        db.session.add(add_livro)
        db.session.commit()
        return redirect (url_for('lista_livro'))
    return render_template("novo_livro.html")

@app.route('/<int:id>/atualiza_livro', methods=["GET","POST"])
def atualiza_livro(id):
    livro_db = livro.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form['Nome']
        descrição = request.form['Descrição']
        valor = request.form['valor']
        livro.query.filter_by(id=id).update({
            
            'name': nome,
            'descrição': descrição,
            'valor': valor
        })
        db.session.commit()
        return redirect(url_for('lista_livro'))

    return render_template(
        'atualiza_livro.html',
        livro=livro_db
    )
    
    
@app.route('/<int:id>/removendo_livros')
def remove_livro(id):
    livro_r= livro.query.filter_by(id=id).first()
    db.session.delete(livro_r)
    db.session.commit()
    return redirect(url_for('lista_livro'))
