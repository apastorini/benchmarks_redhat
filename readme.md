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


Ambiente en Red hat
sudo yum update -y
sudo ln -s /usr/local/bin/python3.12 /usr/bin/python3
[root@vsftpd ~]# sudo mkdir -p /mnt/hgfs
[root@vsftpd ~]# sudo vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
[root@vsftpd ~]# ls /mnt/hgfs/
dnf install python3.12
dnf install python3.12-pip
https://access.redhat.com/documentation/es-es/red_hat_enterprise_linux/9/html/installing_and_using_dynamic_programming_languages/assembly_installing-and-using-python_installing-and-using-dynamic-programming-languages
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo dnf upgrade
sudo yum install snapd
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install pycharm-community --classic


xml
sudo yum install xsltproc
xsltproc style.xsl input.xml -o output.html



open scap
sudo yum install -y openscap-scanner scap-security-guide
sudo oscap xccdf eval --profile xccdf_org.cisecurity.benchmarks_profile_Level_1_Server --results results.xml --report report.html CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml
Limpiar archivo xml
# Crear una copia de seguridad del archivo original
cp CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml.bak

# Usar sed para eliminar caracteres no válidos
sed -i 's/[\x00-\x1F\x7F]//g' CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml


ver perfiles disponibles
oscap info "CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml"

ejecutar perfil
sudo oscap xccdf eval --profile xccdf_org.cisecurity.benchmarks_profile_Level_1_-_Server --results results.xml --report report.html CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml


Level 1 - Workstation: xccdf_org.cisecurity.benchmarks_profile_Level_1_-_Workstation
Level 2 - Workstation: xccdf_org.cisecurity.benchmarks_profile_Level_2_-_Workstation



analisis xml

para cada profile se lsitan las reglas primero

Ejemoplo
 <xccdf:Profile id="xccdf_org.cisecurity.benchmarks_profile_Level_1_-_Server">
    <xccdf:title xml:lang="en">Level 1 - Server</xccdf:title>
    <xccdf:description xml:lang="en">
      <xhtml:p>Items in this profile intend to:</xhtml:p>
      <xhtml:ul>
        <xhtml:li>be practical and prudent;</xhtml:li>
        <xhtml:li>provide a clear security benefit; and</xhtml:li>
        <xhtml:li>not inhibit the utility of the technology beyond acceptable means.</xhtml:li>
      </xhtml:ul>
      <xhtml:p>This profile is intended for servers.</xhtml:p>
    </xccdf:description>

La siguiente es la regla
    <xccdf:select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.1_Ensure_mounting_of_cramfs_filesystems_is_disabled" selected="true"/>
    
Cada regla puede tener varios values

dentro de las rules estàn los  <check system="http://open-scap.org/page/SCE">

que a traves del urn ahcen refrencia al value que  tiene lc òdigo a ejecutar



leer la politica del sistema operativo




https://access.redhat.com/documentation/es-es/red_hat_enterprise_linux/9/html/installing_and_using_dynamic_programming_languages/assembly_installing-and-using-python_installing-and-using-dynamic-programming-languages