<h1 align="center">Watch Museum</h1>

<p align="center">
  <a href="#">
    <img src="https://raw.githubusercontent.com/danhpaiva/watch-museum-react-native/main/logo/Watch-Museum.png" width="500" alt="Watch Museum">
  </a>
</p>
<p align="center">
    BackEnd do aplicativo mobile para gerenciamento de Museu's
</p>

<p align="center">
 <a href="#status">Status</a> • 
 <a href="#objetivo">Objetivo</a> •
 <a href="#instalacao">Instalação</a> • 
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#autor">Autor</a> • 
 <a href="#licenca">Licença</a> 
</p>

<h2 align="center" id=status> 
	:beginner: Concluído :beginner:
</h2>

<h2 id=objetivo>:scroll: Objetivo</h2>

Este projeto tem como objetivo construir o backend da aplicação mobile utilizando Python.<br>
Os códigos "arduino.py" simulam os registros de arduinos.<br>
O arquivo "backup_broker_local.py" salva esses dados no broker local feito em SQLlite.<br>
E os outros arquivos de backup mandam esses dados para o broker remoto (ThingSpeak). <br>
Essa lógica salva os dados de 03 salas do museu na nuvem e localmente.<br>
Caso o sistema fique sem internet, não há problemas pois após salvar os registros localmente, o sistema de vericação irá atuar para assim que a Internet se reestabeleça<br>
Verifique os dados que deverão subir para o broker remoto.<br>
O sistema também registra a média da temperatura diariamente.

<h2 id=instalacao>:clipboard: Instalação</h2>

1. Faça o clone do repositório.
2. Execute o arquivo chamado:
> backup_broker_local.py

Ele registrará o backup local de meia em meia hora.<br>
3. Agora execute o arquivo chamado:
> backup_broker_remoto.py

A cada minuto ele vai checar os dados localmente para mandar para a nuvem.

4. Escolha um horário para que o sistema execute o arquivo diariamente.
5. Para o frontend da aplicação veja este repositório:<br>
[Watch Museum - React Native](https://github.com/danhpaiva/watch-museum-react-native)<br>
6. Clone o repositório.<br>
7. Instale o APK.

<h2 id=tecnologias>:toolbox: Tecnologias</h2>

As seguintes ferramentas foram usadas na construção do projeto:

- IDE: <a href="https://code.visualstudio.com/">Visual Studio Code</a>
- Python 3.7.9 - <a href="https://www.python.org/downloads/release/python-379/"> Download </a>
- Banco de Dados Remoto: <a href="https://thingspeak.com/">ThingSpeak</a>
- Banco de Dados Local: <a href="https://www.sqlite.org/download.html">SQLite 3</a>
- React Native - <a href="https://reactnative.dev/"> Download </a>

<h2 id=autor>:grin: Autores</h2>

Desenvolvido por <a href="https://www.linkedin.com/in/danhpaiva/" target="_blank">Daniel Paiva</a>,
<a href="https://www.linkedin.com/in/francisco-fontoura/" target="_blank">Francisco Fontoura</a>,
<a href="https://github.com/gab-gomes" target="_blank">Gabriel Gomes</a> e 
<a href="https://www.linkedin.com/in/guilhermepujoni/" target="_blank">Guilherme Pujoni</a> .

<h2 id=licenca>:lock: Licença</h2>
<a href="https://github.com/danhpaiva/login-csharp-sqlServer/blob/master/LICENSE" target="_blank">MIT</a>
