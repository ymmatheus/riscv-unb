from utils import settings, instructions, utilities
from simulator import simulator
from assembler import assembler

import os
from flask import Flask, request, render_template, url_for
from flask_cors import CORS, cross_origin
import json
'''
	TODOs:
		instructions.py
			- terminar execute: todas as instruções
			- alinhamento instrucoes

        GUI:
            - Layout geral
                - Menu
                    - Funcoes arquivos
                        - Abrir
                        - Salvar
                        - Novo ( Gerar já um boilerplate com section data section text)

                - Botoes simulacao
                    - Run
                    - Step
                    - Speed

                - Editor de texto
                    - Highlight
                    - Alterar tamanho da fonte
                    - Funcionamento dos Tabs

                - Register Map

                - Memory Map


'''


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("riscv.html")
    #return "aaa"


@app.route("/teste", methods=['GET', 'POST'])
def teste():
    #$.get("http://localhost:8080/teste", function(data,status){alert(data+status)})
    #$.post("http://localhost:8080/teste",{code:1123}, function(data,status){alert(data+status)})
    print("testando")
    if request.method == 'POST':

        print(request.form['code'])

        treta = int(request.form['code'])+10
        return "POST:"+str(treta)
    else:
        return "GET"

@app.route("/assemble", methods=['POST'])
def assemble():
    # o montador retorna um dicionario python com 3 tipos diferentes de dados:
    #   - dados
    #   - codigo
    #   - mensagens de erro

    assmblr_response = assembler.assemble(request.form['code'])

    # retorna o json.dumps do dicionario para ser interpretado no frontend 
    '''assmblr_response = {
        "code":"CODIGOSCODIGOSCODIGOSCODIGOS\nCODIGOSCODIGOSCODIGOSCODIGOS\nCODIGOSCODIGOSCODIGOSCODIGOS\nCODIGOSCODIGOSCODIGOSCODIGOS\nCODIGOSCODIGOSCODIGOSCODIGOS\n",
        "memory":"MEMORIASMEMORIASMEMORIASMEMORIAS\nMEMORIASMEMORIASMEMORIASMEMORIAS\nMEMORIASMEMORIASMEMORIASMEMORIAS\nMEMORIASMEMORIASMEMORIASMEMORIAS\nMEMORIASMEMORIASMEMORIASMEMORIAS\n",
        "errors":"ERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\n"
    }'''
    return json.dumps(assmblr_response)
    #utilities.display_codeobj(cod_obj,"hex")
    #utilities.save_to_file(cod_obj,"mif", r"fileout") 

# 	program_code='''00000000100000000000000110010011
# 11111111111000000000001000010011
# 00000000010000011000001010110011
# 00000000101100000000001100010011   
# 00000001010100110100001110010011
# 00000000100100110110010000010011  
# 00000001001100110111010010010011'''


	#simulator.run(program_code)

	#utilities.display_registers(-1, 'hex')
	#settings.display_memory(0, 100, 'hex')

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT",8080))
    app.run(host='localhost', port=port, debug=True)
    

