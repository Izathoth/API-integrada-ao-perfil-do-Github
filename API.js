// Defina a URL da API (use localhost ou o domínio onde sua API está hospedada)
const urlApi = '...';

// Faz uma requisição para a API usando Fetch
fetch(urlApi)
    .then(response => response.json())
    .then(dados => {
        // Atualiza os elementos HTML com os dados recebidos da API
        document.getElementById('nome').textContent = `Nome: ${dados.nome}`;
        document.getElementById('bio').textContent = `Biografia: ${dados.bio}`;
        document.getElementById('seguidores').textContent = `Seguidores: ${dados.seguidores}`;
        document.getElementById('seguindo').textContent = `Seguindo: ${dados.seguindo}`;
        document.getElementById('estrelas').textContent = `Total de Estrelas: ${dados.total_estrelas}`;
        document.getElementById('repos-publicos').textContent = `Repositórios Públicos: ${dados.repos_publicos}`;
        document.getElementById('url-perfil').innerHTML = `URL do Perfil: <a href="${dados.url_perfil}" target="_blank">${dados.url_perfil}</a>`;

        // Lista os repositórios populares
        const listaRepositoriosPopulares = document.getElementById('repositorios-populares');
        listaRepositoriosPopulares.innerHTML = '';  // Limpa o conteúdo anterior

        dados.repositorios_populares.forEach(repo => {
            const itemRepo = document.createElement('li');
            itemRepo.innerHTML = `<a href="${repo.url}" target="_blank">${repo.nome}</a> - Estrelas: ${repo.estrelas}`;
            listaRepositoriosPopulares.appendChild(itemRepo);
        });
    })
    .catch(error => {
        console.error('Erro ao buscar dados:', error);
    });