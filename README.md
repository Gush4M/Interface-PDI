SIN 392 - Projeto de Processamento de Imagens
Descrição
Este projeto é um sistema interativo para edição e análise de imagens, desenvolvido para a disciplina SIN 392 - Introdução ao Processamento Digital de Imagens da Universidade Federal de Viçosa, Campus Rio Paranaíba. O sistema possui uma interface gráfica (GUI) estilizada com a biblioteca ttkbootstrap e implementa funcionalidades de processamento de imagens em níveis de cinza, incluindo manipulação de histogramas, transformações de intensidade, filtros espaciais e no domínio da frequência, morfologia matemática e segmentação. As operações são aplicadas sequencialmente à imagem processada, permitindo a composição de múltiplas transformações.
Pré-requisitos
Para executar o sistema, você precisará do seguinte:

Sistema Operacional: Windows, macOS ou Linux.
Python: Versão 3.8 ou superior. Recomenda-se a versão mais recente (ex.: 3.11) para melhor compatibilidade.
Gerenciador de Pacotes: pip (geralmente incluído com o Python).
Bibliotecas Python:
pillow: Para manipulação de imagens.
numpy: Para operações numéricas.
ttkbootstrap: Para estilização da interface gráfica.
opencv-python: Para processamento de imagens.
matplotlib: Para exibição de histogramas e espectro de Fourier.
scipy: Para operações no domínio da frequência.

Git (opcional): Para clonar o repositório, se preferir baixá-lo via linha de comando.
Espaço em Disco: Aproximadamente 500 MB para as dependências e o código-fonte.
Memória RAM: Mínimo de 4 GB (recomenda-se 8 GB para imagens grandes).

Configuração do Ambiente
Siga as etapas abaixo para configurar o ambiente necessário para executar o sistema.

1. Instalar o Python

Verifique se o Python está instalado:Abra um terminal (Prompt de Comando no Windows, Terminal no macOS/Linux) e execute:python --version

oupython3 --version

Se a versão exibida for 3.8 ou superior, pule para o próximo passo. Caso contrário, siga as instruções abaixo.
Baixe e instale o Python:
Acesse python.org e baixe a versão mais recente.
Durante a instalação no Windows, marque a opção "Add Python to PATH" para facilitar o uso no terminal.
Após a instalação, verifique novamente a versão com o comando acima.

2. Clonar ou Baixar o Repositório

Opção 1: Clonar via Git:
Instale o Git em git-scm.com se ainda não tiver.
Abra o terminal e execute:git clone https://github.com/Gush4M/Interface-PDI.git

Opção 2: Baixar manualmente:
Acesse o repositório no GitHub, clique em "Code" e selecione "Download ZIP".
Extraia o arquivo ZIP para uma pasta de sua escolha e abra a pasta extraída no terminal:cd caminho/para/a_pasta

3. Criar um Ambiente Virtual (Recomendado)

Crie um ambiente virtual para isolar as dependências:python -m venv venv

Ative o ambiente virtual:
Windows: .\venv\Scripts\activate

macOS/Linux: source venv/bin/activate

Você verá (venv) no início da linha de comando, indicando que o ambiente está ativado.

4. Instalar Dependências\*\*

Com o ambiente virtual ativado, instale as bibliotecas necessárias usando o pip:pip install pillow numpy ttkbootstrap opencv-python matplotlib scipy

Verifique a instalação:Execute:pip list

Confirme que as bibliotecas listadas incluem pillow, numpy, ttkbootstrap, opencv-python, matplotlib, scipy, e tkinter.

5. Verificar o Arquivo do Projeto

Certifique-se de que o arquivo src/main.py está presente no diretório do projeto. Este é o arquivo principal que executa o sistema.

Execução do Sistema
Após configurar o ambiente, siga estas etapas para executar o programa:

Navegue até o diretório do projeto (se ainda não estiver lá):
cd caminho/para/a-pasta

Ative o ambiente virtual (se não estiver ativado):

Windows:.\venv\Scripts\activate

macOS/Linux:source venv/bin/activate

Execute o programa:
python src/main.py

Interaja com o Sistema:

A interface gráfica será aberta.
No menu "Arquivo", selecione "Carregar uma imagem"` para abrir um arquivo de imagem (formatos suportados: PNG, JPG, JPEG, BMP).
Use os botões no painel de funcionalidades para aplicar operações de processamento.
Salve a imagem processada pelo menu "Arquivo" > "Salvar Imagem".
O status da operação será exibido na barra de status abaixo do painel de botões.

Funcionalidades Implementadas

Carregar Imagem: Suporta formatos PNG, JPG, JPEG e BMP. Imagens RGB são convertidas automaticamente para níveis de cinza.
Salvar Imagem: Permite salvar a imagem processada em formato PNG ou JPG.
Histograma: Exibe o histograma da imagem processada em uma janela Matplotlib.
Transformações de Intensidade:
Alargamento de Contraste: Normaliza a intensidade da imagem para a faixa [0, 255].
Equalização de Histograma: Ajusta a distribuição de intensidades para melhorar o contraste.

Filtros Passa-Baixa:
Média: Aplica um filtro de média 5x5.
Mediana: Aplica um filtro de mediana 5x5.
Gaussiano: Aplica um filtro gaussiano 5x5.
Máximo: Aplica um filtro de máximo 3x3.
Mínimo: Aplica um filtro de mínimo 3x3.

Filtros Passa-Alta:
Laplaciano: Detecta bordas usando o operador Laplaciano.
Roberts: Detecta bordas usando máscaras de Roberts.
Prewitt: Detecta bordas usando máscaras de Prewitt.
Sobel: Detecta bordas usando máscaras de Sobel.

Convolução no Domínio da Frequência:
Passa-Baixa: Aplica um filtro circular no domínio da frequência.
Passa-Alta: Aplica um filtro circular complementar no domínio da frequência.

Espectro de Fourier: Exibe o espectro de magnitude da Transformada de Fourier da imagem processada.
Morfologia Matemática:
Erosão: Aplica erosão com um kernel 3x3.
Dilatação: Aplica dilatação com um kernel 3x3.

Segmentação: Aplica o método de Otsu para limiarização automática.
Interface Gráfica: Interface estilizada com ttkbootstrap (tema "flatly"), com botões organizados, labels de status e área de imagem com borda.
Processamento Sequencial: Cada filtro ou transformação é aplicado à imagem processada anteriormente, permitindo composição de operações.

Funcionalidades Pendentes

(Opcional) Descritores de cor, textura e forma com métodos de agrupamento.

Estrutura do Repositório

src/main.py: Código principal da aplicação.
README.md: Instruções de configuração e execução.

Solução de Problemas
Aqui estão soluções para problemas comuns que podem ocorrer durante a configuração ou execução:

Erro: "Python não encontrado":
Certifique-se de que o Python está instalado e adicionado ao PATH. Reinstale o Python e marque "Add Python to PATH" durante a instalação.
Use python3 em vez de python em alguns sistemas Linux/macOS.

Erro: "Módulo não encontrado" (ex.: "No module named 'cv2'"):
Verifique se o ambiente virtual está ativado antes de executar o programa.
Reinstale as dependências com:pip install pillow numpy ttkbootstrap opencv-python matplotlib scipy

Certifique-se de que está usando o pip do ambiente virtual (execute pip --version para confirmar).

Erro ao carregar imagens:
Confirme que as imagens estão em formatos suportados (PNG, JPG, JPEG, BMP).
Evite imagens corrompidas ou com tamanhos muito grandes (>2MB).

Janela Matplotlib não aparece:
Certifique-se de que matplotlib está instalado.
Feche outras janelas abertas do Matplotlib antes de aplicar o histograma ou espectro de Fourier.

Programa lento com imagens grandes:
Redimensione as imagens para 512x512 ou 1024x1024 pixels usando um editor como GIMP ou Photoshop antes de carregar.

Interface gráfica não aparece:
Verifique se tkinter está instalado. No Ubuntu/Debian, instale com:sudo apt-get install python3-tk

No Windows/macOS, tkinter geralmente vem com o Python.

Se encontrar outros problemas, abra uma issue no repositório ou entre em contato com o desenvolvedor.
Como Usar

Execute o programa com:python src/main.py

No menu "Arquivo", selecione "Carregar Imagem" para abrir uma imagem.
A imagem será exibida na área central com borda.
Use os botões no painel de funcionalidades para aplicar as operações de processamento. Cada operação é aplicada à imagem resultante da operação anterior.
No menu "Arquivo", selecione "Salvar Imagem" para salvar a imagem processada.
Para reiniciar o processamento, carregue uma nova imagem.
O status da operação é exibido abaixo do painel de botões.

Recomendações para Testes

Imagens sugeridas:
Lena, Cameraman, Barbara, Peppers, Moon (disponíveis em repositórios como USC-SIPI Image Database ou OpenCV samples).
Imagens de alta resolução com bordas nítidas, texturas ou áreas homogêneas.

Testes recomendados:
Carregue uma imagem e aplique sequencialmente: Filtro Gaussiano, Filtro Sobel e Segmentação Otsu.
Visualize o histograma antes e depois da Equalização de Histograma.
Teste o Alargamento de Contraste com imagens de baixo contraste.

Observações

As imagens devem estar em níveis de cinza para processamento. Imagens RGB são convertidas automaticamente.
O histograma e o espectro de Fourier são exibidos em janelas separadas do Matplotlib.
Para imagens muito grandes, o processamento pode ser lento. Considere redimensioná-las.
O programa foi testado em Windows 10 e Ubuntu 20.04, mas deve funcionar em outros sistemas com as dependências corretas.

Contato
Para dúvidas, sugestões ou relatórios de erros, entre em contato com ou abra uma issue no repositório GitHub.
Licença
Este projeto é para fins acadêmicos e está sob a licença MIT (a menos que especificado otherwise no repositório).
