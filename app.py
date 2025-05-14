


import requests
import configparser


#Habilita capacidades 


from Flask import Flask, render_template, request, redirect, url_for


#Ruta principal
app = Flask(__name__)

#Iniciamos con la logica de la aplicacion 

@app.route ('/')

#Aqui va el nombre de la funcion o metodo que gestiona la ruta 
def weather_dashboard():
    return render_template ('home.html')

@app.route('/results')
 

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']














if __name__ == "__main__":
    app.run(debug=true)
