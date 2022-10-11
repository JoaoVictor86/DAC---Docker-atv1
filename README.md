# DAC---Docker-atv1

  

-   **docker container run tomcat:** comando que irá executar o container do servidor Tomcat;
    
- **docker container ls:** comando que irá listar todos os containers do seu Docker;
    
-   **docker image ls:** comando que irá listar todas as imagens do seu Docker.
    

  

### Criando a imagem Python:

-   $ cd docker-atv
    
-   $ docker build --tag docker-atv .
    
-   $ docker run -d -p 8000:5000 docker-atv

### As vantagens de utilizar os containers do Docker:

- Os containers economizam mais recursos computacionais do que uma Imagem, por exemplo;
- Ele não ocupará muita memória da máquina, fazendo com que possa ser utilizado outros programas enquanto roda;
- Os arquivos podem ser compartilhados entre o container e o host;
- Criar e mudar a infraestrutura é muito mais simples com o container do que com uma imagem.

### Dificuldades:
- Não consegui rodar a aplicação na rota 8080:8080, mas na 8000:5000 sim.
