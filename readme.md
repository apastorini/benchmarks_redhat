# Benchmark Project

Este proyecto realiza verificaciones de benchmark para Red Hat Enterprise Linux 8.

## Requisitos

- Python 3.8 o superior
- `pip` para instalar dependencias

## Instalación

1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt


## Instalar Python en Red Hat
sudo yum update -y
2. Instalar las Dependencias Necesarias
Instala las dependencias necesarias para compilar Python desde el código fuente.

bash
Copiar código
sudo yum groupinstall -y "Development Tools"
sudo yum install -y openssl-devel bzip2-devel libffi-devel zlib-devel wget
3. Descargar el Código Fuente de Python 3.12
Descarga el tarball del código fuente de Python 3.12 desde el sitio oficial de Python.

bash
Copiar código
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz
4. Extraer el Código Fuente
Extrae el archivo tarball descargado.

bash
Copiar código
sudo tar xzf Python-3.12.0.tgz
cd Python-3.12.0
5. Compilar e Instalar Python 3.12
Configura, compila e instala Python 3.12.

bash
Copiar código
sudo ./configure --enable-optimizations
sudo make altinstall
La opción --enable-optimizations optimiza la compilación para mejorar el rendimiento. El uso de make altinstall en lugar de make install evita que sobrescriba la instalación de Python predeterminada del sistema.

6. Verificar la Instalación
Verifica que Python 3.12 se haya instalado correctamente.

bash
Copiar código
python3.12 --version
Deberías ver una salida similar a:

plaintext
Copiar código
Python 3.12.0
7. Opcional: Crear un Enlace Simbólico
Si deseas poder usar python3 para invocar Python 3.12, puedes crear un enlace simbólico.

bash
Copiar código
sudo ln -s /usr/local/bin/python3.12 /usr/bin/python3
Alternativa: Usar pyenv
Otra opción es usar pyenv, una herramienta que permite gestionar múltiples versiones de Python en el mismo sistema.

Instalación de pyenv
Instalar Dependencias:

bash
Copiar código
sudo yum install -y git gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel
Instalar pyenv:

bash
Copiar código
curl https://pyenv.run | bash
Agrega las siguientes líneas a tu archivo de configuración de shell (~/.bashrc o ~/.zshrc):

bash
Copiar código
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
Recarga tu shell:

bash
Copiar código
source ~/.bashrc
Instalar Python 3.12:

bash
Copiar código
pyenv install 3.12.0
pyenv global 3.12.0
Verificar la Instalación:

bash
Copiar código
python --version

