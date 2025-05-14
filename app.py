


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
def render_results():
    cityname  = request.form['cityname']
    


# esta variable esta almacenando el valor de la api key    
api = get_api_key();


#vamos a conectarlo al api y consumirla

data = get_weather_results(cityname, api)
#se toma la temperatura del json
temp = "{0:.2f}".format(data['main']['temp'] - 273.15)
    

    return render_template('results.html', cityname=cityname, temp=temp, humidity=humidity, pressure=pressure, wind=wind, description=description, icon=icon)

def get_weather_results(cityname, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cityname, api_key)
    r = requests.get(url)
    return r.json()
   
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']












if __name__ == "__main__":
    app.run(debug=true)
