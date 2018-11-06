# Instalação: #

1 - Executar: ```sudo docker-compose up -d --build --remove-orphans``` e aguardar a inicialização do banco de dados;

2 - Entrar no bash do app e fazer as migrações do Django:

- ```sudo docker-compose exec app bash```
- ```python manage.py makemigrations```
- ```python manage.py migrate```
- ```python manage.py createsuperuser```

3 - Sair do bash e reiniciar o container: ```sudo docker-compose restart app```