# SIN 392 - Projeto de Processamento de Imagens

## Descrição

Este projeto é um sistema interativo para edição e análise de imagens, desenvolvido para a disciplina **SIN 392 - Introdução ao Processamento Digital de Imagens** da Universidade Federal de Viçosa, Campus Rio Paranaíba. O sistema possui uma interface gráfica (GUI) estilizada com a biblioteca `ttkbootstrap` e implementa funcionalidades de processamento de imagens em níveis de cinza, incluindo manipulação de histogramas, transformações de intensidade, filtros espaciais e no domínio da frequência, morfologia matemática e segmentação. As operações são aplicadas sequencialmente à imagem processada, permitindo a composição de múltiplas transformações.

---

## Pré-requisitos

Para executar o sistema, você precisará dos seguintes itens:

- **Sistema Operacional**: Windows, macOS ou Linux.
- **Python**: Versão 3.8 ou superior (recomenda-se 3.11 para melhor compatibilidade).
- **Gerenciador de Pacotes**: `pip` (geralmente incluído com o Python).
- **Bibliotecas Python**:
  - `pillow`: Manipulação de imagens.
  - `numpy`: Operações numéricas.
  - `ttkbootstrap`: Estilização da interface gráfica.
  - `opencv-python`: Processamento de imagens.
  - `matplotlib`: Exibição de histogramas e espectro de Fourier.
  - `scipy`: Operações no domínio da frequência.
- **Git** (opcional): Para clonar o repositório via linha de comando.
- **Espaço em Disco**: Aproximadamente 500 MB para dependências e código-fonte.
- **Memória RAM**: Mínimo de 4 GB (recomenda-se 8 GB para imagens grandes).

---

## Configuração do Ambiente

Siga as etapas abaixo para configurar o ambiente necessário para executar o sistema.

### 1. Instalar o Python

1. **Verifique se o Python está instalado**:
   Abra um terminal (Prompt de Comando no Windows, Terminal no macOS/Linux) e execute:

   ```bash
   python --version
   ```

   ou

   ```bash
   python3 --version
   ```

   Se a versão exibida for 3.8 ou superior, vá para o próximo passo. Caso contrário, siga as instruções abaixo.

2. **Baixe e instale o Python**:
   - Acesse [python.org](https://www.python.org/downloads/) e baixe a versão mais recente.
   - **Windows**: Durante a instalação, marque a opção "Add Python to PATH" para facilitar o uso no terminal.
   - Após a instalação, verifique novamente a versão com o comando acima.

### 2. Clonar ou Baixar o Repositório

- **Opção 1: Clonar via Git**:

  1. Instale o Git em [git-scm.com](https://git-scm.com/downloads) se ainda não tiver.
  2. Abra o terminal e execute:
     ```bash
     git clone https://github.com/Gush4M/Interface-PDI.git
     ```
  3. Navegue até o diretório do projeto:
     ```bash
     cd Interface-PDI
     ```

- **Opção 2: Baixar manualmente**:
  1. Acesse o repositório no GitHub, clique em "Code" e selecione "Download ZIP".
  2. Extraia o arquivo ZIP para uma pasta de sua escolha.
  3. Abra o terminal e navegue até a pasta extraída:
     ```bash
     cd caminho/para/a-pasta
     ```

### 3. Criar um Ambiente Virtual (Recomendado)

1. Crie um ambiente virtual para isolar as dependências:

   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
     Após ativar, você verá `(venv)` no início da linha de comando.

### 4. Instalar Dependências

1. Com o ambiente virtual ativado, instale as bibliotecas necessárias:

   ```bash
   pip install pillow numpy ttkbootstrap opencv-python matplotlib scipy
   ```

2. **Verifique a instalação**:
   Execute:
   ```bash
   pip list
   ```
   Confirme que as bibliotecas listadas incluem `pillow`, `numpy`, `ttkbootstrap`, `opencv-python`, `matplotlib`, `scipy` e `tkinter`.

### 5. Verificar o Arquivo do Projeto

- Certifique-se de que o arquivo `image_processing_gui.py` está presente no diretório do projeto. Este é o arquivo principal que executa o sistema.

---

## Execução do Sistema

Após configurar o ambiente, siga estas etapas para executar o programa:

1. **Navegue até o diretório do projeto**:

   ```bash
   cd caminho/para/a-pasta
   ```

2. **Ative o ambiente virtual** (se não estiver ativado):

   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Execute o programa**:

   ```bash
   python image_processing_gui.py
   ```

4. **Interaja com o Sistema**:
   - A interface gráfica será aberta.
   - No menu **Arquivo**, selecione **Carregar Imagem** para abrir um arquivo de imagem (formatos suportados: PNG, JPG, JPEG, BMP).
   - Use os botões no painel de funcionalidades para aplicar operações de processamento.
   - Salve a imagem processada pelo menu **Arquivo** > **Salvar Imagem**.
   - O status da operação será exibido na barra de status abaixo do painel de botões.

---

## Funcionalidades Implementadas

| Funcionalidade                          | Descrição                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------- |
| **Carregar Imagem**                     | Suporta PNG, JPG, JPEG e BMP. Imagens RGB são convertidas para níveis de cinza. |
| **Salvar Imagem**                       | Salva a imagem processada em PNG ou JPG.                                        |
| **Histograma**                          | Exibe o histograma da imagem processada em uma janela Matplotlib.               |
| **Alargamento de Contraste**            | Normaliza a intensidade para a faixa [0, 255].                                  |
| **Equalização de Histograma**           | Ajusta a distribuição de intensidades para melhorar o contraste.                |
| **Filtros Passa-Baixa**                 | Média (5x5), Mediana (5x5), Gaussiano (5x5), Máximo (3x3), Mínimo (3x3).        |
| **Filtros Passa-Alta**                  | Laplaciano, Roberts, Prewitt, Sobel.                                            |
| **Convolução no Domínio da Frequência** | Passa-Baixa e Passa-Alta com filtro circular.                                   |
| **Espectro de Fourier**                 | Exibe o espectro de magnitude da Transformada de Fourier.                       |
| **Morfologia Matemática**               | Erosão e Dilatação com kernel 3x3.                                              |
| **Segmentação Otsu**                    | Aplica limiarização automática com o método de Otsu.                            |
| **Interface Gráfica**                   | Estilizada com ttkbootstrap (tema "vapor"), com botões e status.               |
| **Processamento Sequencial**            | Operações são aplicadas à imagem processada anteriormente.                      |

---

## Estrutura do Repositório

- `image_processing_gui.py`: Código principal da aplicação.
- `README.md`: Instruções de configuração e execução.

---

## Como Usar

1. Execute o programa com:

   ```bash
   python image_processing_gui.py
   ```

2. No menu **Arquivo**, selecione **Carregar Imagem** para abrir uma imagem.
3. A imagem será exibida na área central com borda.
4. Use os botões no painel de funcionalidades para aplicar operações. Cada operação é aplicada à imagem resultante da anterior.
5. Salve a imagem processada com **Arquivo** > **Salvar Imagem**.
6. Para reiniciar, carregue uma nova imagem.
7. O status da operação é exibido abaixo do painel de botões.

---

## Contato

Para dúvidas, sugestões ou relatórios de erros, entre em contato com `gustavo.reis@ufv.br` ou abra uma [issue](https://github.com/<seu-usuario>/<nome-do-repositorio>/issues) no GitHub.
