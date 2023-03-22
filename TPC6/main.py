import ply.lex as lex

# ! Tokens ! #

tokens = (
    'TIPO',
    'VARIAVEL',
    'FUNCAO',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PAROPEN',
    'PARCLOSE',
    'CURVOPEN',
    'CURVCLOSE',
    'RETOPEN',
    'RETCLOSE',
    'VIRGULA',
    'PONTOVIRG',
    'ATRIB',
    'EQUALS',
    'MENOR',
    'MAIOR',
    'COMMENT',
    'COMMENTBLOCK',
    'RETS',
    'CICLO'
)

t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PAROPEN = r'\('
t_PARCLOSE = r'\)'
t_CURVOPEN = r'{'
t_CURVCLOSE = r'}'
t_RETOPEN = r'\['
t_RETCLOSE = r'\]'
t_VIRGULA = r'\,'
t_PONTOVIRG = r'\;'
t_ATRIB = r'\='
t_EQUALS = r'\={2}'
t_MENOR = r'\<'
t_MAIOR = r'\>'
t_RETS = r'\.{2,}'

def t_CICLO(t):
    r'(for|while)'
    return t

def t_FUNCAO(t):
    r'[a-z][a-zA-Z0-9_]*\(|[a-z][a-zA-Z0-9_]*\{'
    return t

def t_TIPO(t):
    r'(int|float|char|double|long|short|void|string|bool|vector|program|function)'
    return t

def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_MINUS(t):
    r'\-'
    return t

def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'//.*\n'
    return t

def t_COMMENTBLOCK(t):
    r'/\*(.|\n)*?\*/'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carater Ilegal {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

# ! Exemplo 1 ! #

print("\n+" + "-" * 55 + "+")
print("|\t\t\tExemplo 1\t\t\t|")
print("+" + "-" * 55 + "+\n")

exemplo1 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

lexer.input(exemplo1)

for token in lexer:
    print(token)

# ! Exemplo 2 ! #

print("\n+" + "-" * 55 + "+")
print("|\t\t\tExemplo 2\t\t\t|")
print("+" + "-" * 55 + "+\n")

exemplo2 = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

lexer.input(exemplo2)

for token in lexer:
    print(token)

print("\n+" + "-" * 55 + "+")
print("|\t\t\t   FIM   \t\t\t|")
print("+" + "-" * 55 + "+\n")