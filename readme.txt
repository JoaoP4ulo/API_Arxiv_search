A ideia deste projeto é desenvolver usando a linguagem de programação Python um
sistema de recuperação de artigos científicos usando a Application Programming
Interface (API) do Arxiv1. O Arxiv é um repositório contendo artigos científicos de
diversas áreas do conhecimento como, Matemática, Engenharia, Computação, Física,
entre outros. 

Estrutura organizacional:

---main---
- definição de variaveis base
- construção do data-base
- chamada inicial 

---utils---
- funções que não envolvem o data-base

---classes_base---
- definição das classes padrões

---classes_dao---
- definição dos Objetos de Acesso a Dados

---controlador_menu---
- chamar as funções relacionadas ao primeiro menu

---controlador_sistema---
- chamar as funções relacionadas ao segundo menu