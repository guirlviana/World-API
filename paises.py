import requests, json



def request(url):

    resp = requests.get(url)
    if resp.status_code == 200:
        resultado = json.loads(resp.text)
        if resultado:
            return resultado

def help():
    print("COMANDOS:\n-n = nome\n-c = capital\n-p = população\n-r = região\n-m = moeda\n-a = todos")

def addOptions(option):
    plus_url = ''
    if option == '-n':
        plus_url = 'name;'
    
    elif option == '-c':
        plus_url = 'capital;'
    
    elif option == '-p':
        plus_url = 'population;'
    
    elif option == '-r':
        plus_url = 'region;'
    
    elif option == '-m':
        plus_url = 'currencies;'
    
    elif option == '-a':
        plus_url = 'name;capital;population;region;currencies;'
        
    else:
        print(f"{option} <= opção inválida digite -ajuda para ver todos os comandos")
    
    return plus_url

def showValues(dict_values):
    from tabulate import tabulate
    info_list = []
    for k, i in dict_values.items():
        if type(i) is list:
            for k, i in i[0].items():
                info_list.append([k,i])
        else:
            info_list.append([k,i])
    
    
    print(tabulate(info_list,headers=['Info', 'Dado'], tablefmt="psql"))
                                


if __name__ == "__main__":
    while True:
        
        command = str(input(': ')).split(' ')
        
        if '-world' not in command:
            print('Comando inválido')
        else:
            if '-ajuda' in command:
                help()
            elif '-sair' in command:
                break
            else:
                try:
                    country_name = command[1]
                    url = f'https://restcountries.eu/rest/v2/name/{country_name}?fields='
                    for option in range (2, len(command)):
                        url_option = addOptions(command[option])
                        url += url_option
                    resultados = request(url)
                    showValues(resultados[0])
            
                except Exception:
                    pass
            