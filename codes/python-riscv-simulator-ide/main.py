# -*- coding: utf-8 -*-

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
			- terminar execute: todas as instrucoes
			- alinhamento instrucoes

        GUI:
            - Layout geral
                - Menu
                    - Funcoes arquivos
                        - Abrir
                        - Salvar
                        - Novo ( Gerar ja um boilerplate com section data section text)

                - Botoes simulacao
                    - Run
                    - Step
                    - Speed

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
    
    # Assembler will return MEMORY, CODE, and ERRORS data.
    assmblr_response = assembler.assemble(request.form['code'])    

    data_dump = {

        "code":{
            "bin":assmblr_response['code'],
            "hex":utilities.dump_convert(assmblr_response['code'],"hex"),
            "mif":utilities.dump_convert(assmblr_response['code'],"mif")        
        },


        "memory":{
            "bin":assmblr_response['memory'],
            "hex":utilities.dump_convert(assmblr_response['memory'],"hex"),            
            "mif":utilities.dump_convert(assmblr_response['memory'],"mif")
        },

        "errors": assmblr_response['errors']
        
    }

    # retorna o json.dumps do dicionario para ser interpretado no frontend 
    '''
    assmblr_response = {
        "code":{"bin":["010100101","1010101"], "hex":["12e2e","abcd871"]},
        "memory":{"bin":["02020202","02020202","02020202","02020202","02020202",], "hex":["d8f7ba"]},
        "errors":["ERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\nERROERROERROERROERROERRO\n"]
    }
    '''
    #print(assmblr_response['code'])
    #print(utilities.dump_convert(assmblr_response['code'],"hex") )

    #utilities.save_to_file(data_dump['memory']['bin'],"mem")
    #utilities.save_to_file(data_dump['code']['bin'],"cod")



    return json.dumps(data_dump)


if __name__ == "__main__":
    
    port = int(os.environ.get("PORT",8080))
    app.run(host='localhost', port=port, debug=True)
    

