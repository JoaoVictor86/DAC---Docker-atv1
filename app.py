from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def main():
  resultado = 'Entre as notas na URL'    

  primeira = request.args.get('primeira')
  segunda = request.args.get('segunda')

  if primeira and segunda:
        
    primeira = float(primeira)
    segunda = float(segunda)

    media = (primeira + segunda) / 2
    if media >= 7:
        resultado = 'Aprovado'
    elif media >= 4:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado'

  return resultado

if __name__ == '__main__':
  app.run(debug=True)
