# Exposição Virtual de Coleções, Autenticação e Testes Automatizados

Este é um sistema de gerenciamento de exposições virtuais de coleções de livros, desenvolvido como parte da Trilha 9 - Desenvolvimento Back-End (Python) do programa Residência em TIC36. Ele permite que os usuários criem, gerenciem e compartilhem suas próprias coleções de livros, com autenticação baseada em Token e controle de permissões. O sistema também oferece documentação detalhada da API e testes automatizados para garantir a confiabilidade das funcionalidades.

---

## Desenvolvido por:
- Beatriz Oliveira Freitas
- Manoel Barbosa da Silva Filho  

---

## Funcionalidades:
- **Gerenciamento de Coleções**: Criação, listagem, edição e exclusão de coleções associadas a um usuário (colecionador).
- **Controle de Permissões**:
  - Apenas o colecionador pode modificar ou excluir suas coleções.
  - Outros usuários podem visualizar e listar coleções públicas.
- **Autenticação baseada em Token**: Garante que somente usuários autenticados possam acessar e modificar coleções.
- **Documentação da API**: Desenvolvida com `drf-spectacular`.
- **Testes Automatizados**: Validação da criação, associação de coleções, permissões e visibilidade de dados.
- **Configuração de CORS**: Permite o consumo da API por clientes externos.
- **Requisitos do Projeto**: Gerenciamento automatizado com o arquivo `requirements.txt`.

---

## Tecnologias Utilizadas:
- Python
- Django
- Django Rest Framework (DRF)
- Django Filter
- drf-spectacular
- django-cors-headers
- coverage.py (para cobertura de testes)

---

## Passos de Desenvolvimento:
1. **Modelo de Coleção**:
   - Implementação do modelo `Colecao` com relacionamento ao usuário autenticado.
   - Definição de permissões personalizadas para o gerenciamento de coleções.
2. **Autenticação**:
   - Configuração de autenticação baseada em Token.
   - Permissões ajustadas para colecionadores.
3. **Documentação da API**:
   - Configuração do `drf-spectacular` para endpoints e schemas.
4. **Testes Automatizados**:
   - Validação de todas as funcionalidades relacionadas às coleções.
   - Cobertura do código usando `coverage.py`.
5. **Configuração de CORS**:
   - Uso de `django-cors-headers` para permitir acesso externo.
6. **Versionamento**:
   - Arquivo `.gitignore` configurado para boas práticas de versionamento.
