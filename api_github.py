from fastapi import FastAPI
import requests

app = FastAPI()

# URL da API do GitHub e o nome de usuário a ser consultado
GITHUB_API_URL = "https://api.github.com"
USERNAME = "Soradevs"  # Substitua pelo seu username do GitHub

# Função que coleta os dados do perfil do GitHub
def obter_dados_github():
    # Faz as requisições para os endpoints da API do GitHub
    url_usuario = f"{GITHUB_API_URL}/users/{USERNAME}"
    url_repositorios = f"{GITHUB_API_URL}/users/{USERNAME}/repos"
    
    dados_usuario = requests.get(url_usuario).json()
    dados_repositorios = requests.get(url_repositorios).json()
    
    # Informações básicas do perfil
    seguidores = dados_usuario.get('followers', 0)
    seguindo = dados_usuario.get('following', 0)
    url_perfil = dados_usuario.get('html_url', '')
    bio = dados_usuario.get('bio', 'Sem biografia disponível')
    nome = dados_usuario.get('name', 'Sem nome disponível')
    repos_publicos = dados_usuario.get('public_repos', 0)

    # Soma o total de estrelas de todos os repositórios
    total_estrelas = sum(repo.get('stargazers_count', 0) for repo in dados_repositorios)

    # Ordena os repositórios por estrelas e pega os 5 mais populares
    repos_populares = sorted(dados_repositorios, key=lambda x: x['stargazers_count'], reverse=True)[:5]
    repositorios_populares = [{"nome": repo['name'], "estrelas": repo['stargazers_count'], "url": repo['html_url']} for repo in repos_populares]
    
    # Retorna os dados organizados em um dicionário
    return {
        "nome": nome,
        "bio": bio,
        "seguidores": seguidores,
        "seguindo": seguindo,
        "total_estrelas": total_estrelas,
        "repos_publicos": repos_publicos,
        "url_perfil": url_perfil,
        "repositorios_populares": repositorios_populares
    }

# Rota da API para obter os dados do perfil do GitHub
@app.get("/dados-github")
def dados_github():
    dados = obter_dados_github()
    return dados