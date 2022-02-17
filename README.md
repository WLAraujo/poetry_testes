# poetry_testes

Repositório com alguns testes de uso da ferramenta poetry, uma ferramenta para empacotamento e gestão de dependências de projetos python. 

O poetry é uma ferramenta muito prática e simples de usar que nos permite:
* Controlar bem ambientes de desenvolvimento
* Criar pacotes através de builds muito simples
* Compartilhar o trabalho no pypi de maneira fácil
* Rastrear as dependências de nossa aplicação

Passos para usar o poetry:
1. Primeiro precisamos instalar o poetry através de `pip install poetry`.
2. Para ver os comandos disponíveis com poetry use `poetry help`.
3. Para criar um novo projeto digite `poetry new <nome do projeto>`, isso criará uma estrutura básica de projeto para desenvolvimento igual a seguinte.
```
├──<nome do projeto> ---> Diretório onde o comando ´poetry new <nome do projeto>´ foi executado
    └──<nome do projeto> ---> Diretório onde todo o código deve ser mantido
        └──__init.py__ ---> Local onde a versão do pacote deve ser marcada
    └──tests ---> Onde os testes unitários da biblioteca devem ser realizados
    └──pyproject.toml ---> Onde as dependências do projeto devem ser evidênciadas
    └──readme.rst ---> Arquivo para documentar o pacote através de reStructured Text uma linguagem markup
```
4. Caso seja necessário adicionar alguma dependência pela linha de comando use `poetry add <dependência>`. Após adicionarmos a primeira dependência o poetry criará o `poetry.lock` que é onde as versões de dependências serão mantidas.
5. Para verificar se todas as dependências estão coerentes e batendo usamos o `poetry check`.
6. Se tudo estiver certo no check já podemos usar o `poetry build` que vai criar os arquivos `.tar.gz` e `.whl`. 
7. Por fim, para finalmente publicarmos o pacote no pypi usamos `poetry publish`. Uma observação é que para publicar o pacote é necessário uma conta no pypi.

Ao fim, o seu projeto deve ter uma estrutura semelhante à seguinte:
```
├──<nome do projeto> ---> Diretório onde o comando ´poetry new <nome do projeto>´ foi executado
    └──<nome do projeto> ---> Diretório onde todo o código deve ser mantido
        └──__init.py__ ---> Local onde a versão do pacote deve ser marcada
    └──tests ---> Onde os testes unitários da biblioteca devem ser realizados
    └──dist ---> Onde os arquivos de build são mantidos
    └──pyproject.toml ---> Onde as dependências do projeto devem ser evidênciadas
    └──readme.rst ---> Arquivo para documentar o pacote através de reStructured Text uma linguagem markup
    └──poetry.lock ---> Onde as versões corretas das dependências são mantidas em hash
```
É possível ver que o pacote criado e publicado de exemplo nesse repositório (localizado na pasta `projeto_teste`) possui estrutura semelhante à mostrada acima.

O pacote criado nesse repositório é visa ser uma cacluladora simples com as operações de soma, subtração, multiplicação e divisão. O pacote já foi publicado no pypi na versão 0.1.0, para instalá-lo use `pip install projeto-teste` e para importá-lo use `import projeto_teste`.

No jupyter notebook `caderno_teste.ipynb` temos uma demonstração de uso do pacote.