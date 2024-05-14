class pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def saudacao(self):
        print("Bem vindx", self.nome, "\nSua idade:", self.idade, "\nSeu e-mail:", self.email)
        
humano = pessoa(nome= input("Qual seu nome: "), idade=int(input("Qual sua idade: ")), email=input("Qual seu email: "))
humano.saudacao()

class livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
    def detalhes(self):
        print("O livro", self.titulo, "foi publicado por", self.autor, "no ano", self.email)
livros = livro(titulo= input("Qual o titulo do livro: "), autor=input("Qual o autor do livro: "), ano_publicado=int(input("Qual ano foi publicado: ")))
livros.detalhes()