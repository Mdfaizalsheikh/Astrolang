import re

#token
token_lang= [
  ('NUMBER',   r'\d+(\.\d+)?([eE][+-]?\d+)?'),   #int, float
  ('ID', r'[A-Za-z]\w*') ,#alphabet
  ('ASSIGN', r'='), 
  ('OP', r'[+\-*/]'), #operators
  ('Keywords', r'\b(nebula|galaxy|star|sun|moon|planet|dwarf|transmit') , #keywords
  ('LPAREN', r'\(') , 
  ('RPAREN', r'\) '), 
  ('LBRACE', r'\{'), 
  ('RBRACE', r'\}'),
  ('SKIP', r'[ \t]+'), 
  ('MISTMATCH', r'.'), 
  ('NEWLINE', r'/n'),#newline
  ('COMMENT', r'***'), 


  
]

master_pattern = re.compile(r'|'.join('(?P<%s>%s) ' % pair for pair in token_lang))

def generate_tokens(pattern,text):
  line_num=1
  line_start=0

  for match in pattern.finder(pattern,text):
    kind=match.lastgroup
    value=match.group(kind)

    if kind =='NUMBER':
      value = float(value) 
    
    elif kind =='ID' and value in {'nebula','galaxy','star','sun','moon','planet','dwarf','transmit'}:

      kind = 'keywords'

    elif kind=='NEWLINE':
      line_start= match.end()
      line_num +=1
      continue

    elif kind=='SKIP' or kind=='COMMENT':
      continue 

    elif kind=='MISMATCH':
      raise RuntimeError(f"{value!r} unexpected on line {line_num}")

    yield kind, value

code= "yaha code likhna hai"

tokens =generate_tokens(master_pattern,code)

for token in tokens:
  print (token)


      
    
    
