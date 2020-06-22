from flask import render_template, redirect, request, flash
from app import app
from app.helpers.helper_cadastro import verifica_usuario, cria_usuario
from app.helpers.helper_login import valida_login, busca_usuario_id
from app.helpers.helper_docentes import lista_docentes, busca_professor, media_avaliacoes, ultima_avaliacao, top3
from app.helpers.helper_avaliacao import cria_avaliacao, altera_avaliacao, verifica_avaliacao_professor

@app.route('/')
def login():
    return render_template(
        'login.html',
        titulo = 'Faça seu login | Avalia Aqui!',
        css = 'login.css'
    )

@app.route('/logar', methods=['GET', 'POST'])
def logar():
    usuario = request.form['input_usuario']
    senha = request.form['input_senha']
    login_db = valida_login(usuario, senha)
    if login_db:
        return render_template(
            'docentes.html',
            titulo = 'Docentes | Avalia Aqui!',
            professores = lista_docentes(),
            css = 'docentes.css',
            usuario = login_db,
            top3 = top3()
        )
    else:
        flash('Usuário inexistente ou senha incorreta.')
        return redirect('/')


@app.route('/cadastro', methods=['GET', 'POST', ])
def cadastro():
    return render_template(
        'cadastro.html',
        titulo = 'Faça seu cadastro | Avalia Aqui!',
        css = 'cadastro.css'
    )

@app.route('/cadastrar', methods=['GET', 'POST', ])
def cadastrar():
    valido = False # Variável de cadastro. Inicialmente o cadastro é declarado como inválido.
    usuario = request.form['input_usuario']
    senha = request.form['input_senha']
    rep_senha = request.form['input_rep_senha']
    if not verifica_usuario(usuario):
        if senha == rep_senha:
            valido = True
            cria_usuario(usuario, senha)
            flash('Usuário criado com sucesso!')
        else:
            flash('Senhas não coincidem.')
    else: 
        flash('Usuário já existe.')

    if valido:
        return redirect('/')
    else:
        return redirect('/cadastro')

@app.route('/professor/<id_usuario>/<id_professor>', methods=['GET', ])
def professor(id_usuario, id_professor):
    return render_template(
        'professor.html',
        titulo = 'Avalie o professor!',
        css = 'professor.css',
        professor = busca_professor(id_professor),
        id_usuario = id_usuario,
        media_avaliacoes = media_avaliacoes(id_professor),
        ultima_avaliacao = ultima_avaliacao(id_usuario, id_professor)
    )

@app.route('/avaliar/<id_usuario>/<id_professor>', methods=['GET', 'POST' ])
def avaliar(id_usuario, id_professor):
    nota1 = request.form['nota1']
    nota2 = request.form['nota2']
    nota3 = request.form['nota3']
    nota4 = request.form['nota4']
    nota5 = request.form['nota5']
    if verifica_avaliacao_professor(id_usuario, id_professor):
        flash('Avaliação alterada com sucesso!')
        altera_avaliacao(nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor)
    else:
        flash('Avaliação concluída com sucesso!')
        cria_avaliacao(nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor)

    return render_template(
            'docentes.html',
            titulo = 'Docentes | Avalia Aqui!',
            professores = lista_docentes(),
            css = 'docentes.css',
            usuario = busca_usuario_id(id_usuario),
            top3 = top3()
        )

@app.route('/deslogar')
def deslogar():
    return redirect('/')


