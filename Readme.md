# Concursos No Brasil Website Scrapper 
  API retorna todos os concursos públicos no Brasil.

## Do Uso
  Esse projeto tem caráter educativo e usa matérias publicadas no website [ConcursosNoBrasil.com](https://concursosnobrasil.com) como fonte de dados. Todo conteúdo utilizado é de propriedade e responsabilidade do site [ConcursosNoBrasil.com](https://concursosnobrasil.com).

  Modificações nas estruturas de página no site de onde são extraídas as informações podem causar indisponibilidade da API, problema que afeta a maioria de aplicações que usam webScraping para adquirir dados.

  Portanto recomenda-se __NÃO USAR EM PRODUÇÃO__.

## Tecnologias
  * Flask - É um framework que torna possível criar o servidor web e gerenciar rotas, o que permite a criação de API.
  
  * BeautifulSoup 4 - Permite fazer o webScraping do website.

## API
  | ROTA | MÉTODO | DESCRIÇÃO |
  | --- | --- | --- |
  | /concursos/\<CATEGORIA> | GET | Retorna todos os concursos em uma categoria, onde \<CATEGORIA> é um código de duas letras.  |
  | / | - |  Rota base da API, retorna uma mensagem caso o servidor esteja funcionando.| 

  ### Códigos de Categoria
  Código de duas letras que representa uma categoria no site concursosDoBrasil.

  | CÓDIGO | CATEGORIA |
  | --- | --- |
  | br | Nacional | 
  | ac | Acre |
  | al | Alagoas |
  | am | Amazônas | 
  | ap | Amapá |
  | ba | Bahia | 
  | ce | Ceará | 
  | df | Distrito Federal |
  | es | Espírito Santo |
  | go | Goiás | 
  | ma | Maranhão | 
  | mg | Minas Gerais |
  | ms | Masto Grosso do Sul |
  | mt | Mato Grosso | 
  | pa | Pará |
  | pb | Paraíba | 
  | pe | Pernambuco | 
  | pi | Piauí |
  | pr | Paraná | 
  | rj | Rio de Janeiro |
  | rn | Rio Grande do Norte | 
  | ro | Rondônia | 
  | rr | Rorâima | 
  | rs | Rio Grande do Sul | 
  | sc | Santa Catarina |
  | se | Sergipe |
  | sp | São Paulo |
  | to | Tocantins |

## Estruturas de Dado
  ### Concurso
  ```Json
  {
    "link": "https://......",
    "organization": "Banco Estadual X",
    "status": "open",
    "workPlacesAvailable": "7.000"
  }
  ```
  | CHAVE | TIPO | DESCRIÇÃO |
  | --- | --- | --- |
  | link | str | Url que aponta para a máteria no site. |
  | organization | str | Nome da organização para onde a vaga foi aberta |
  | status | "open" \| "closed" \| "expected" | REpresenta o estatus do concurso, _open_ para concurso aberto, _closed_ para encerrado e _expected_ para concurso que não está aberto mas é experado para ser aberto (tipo o da abin que tem um bilhão de anos que não abre). | 
  | workPlacesAvailable | str \| "Várias" | Representa o número de vágas públicado do concurso segundo a matéria. |

