# Benchmark Project

Este proyecto realiza verificaciones de benchmark para Red Hat Enterprise Linux 8.

## Requisitos

- Python 3.12
- `pip` para instalar dependencias
- Git para descargar repositorio

## Estructrura del git
-En la rama main se encuentra la ùltima versiòn del còdigo
-en la rama nueva_rama, se encuentran los scripts de pruena que se realizaron durante la etata de investigaciòn
preferentemente el parseo del xml de CIS


## Instalaciòn python Sistema operativo
De: https://access.redhat.com/documentation/es-es/red_hat_enterprise_linux/9/html/installing_and_using_dynamic_programming_languages/assembly_installing-and-using-python_installing-and-using-dynamic-programming-languages
sudo yum update -y
sudo yum install -y git gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel
Recargar shell:source ~/.bashrc
dnf install python3.12
dnf install python3.12-pip
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo dnf upgrade

Si es necesaio crear un enlace sìmbolico:
sudo ln -s /usr/local/bin/python3.12 /usr/bin/python3



## Descargar y ejecutar el código
1. Clona el repositorio, la rama main.
2. Navega al directorio del proyecto.
3. Dentro de la carpeta benchmark_script crear un entorno virtual
python3 -m venv venv (el comando python puede ser python3.12, segùn se haya hecho el enlace sìmbolico o no. se debe agregar python y pip al path)
El entorno virtual se activa con: venv\Scripts\activate         
4. Instalar las dependencias:
      pip install -r requirements.txt
5. Ejecutar còdigo:
 ./main.py


## (Opcional) Obtener una carpeta compartida del host principal
sudo mkdir -p /mnt/hgfs
sudo vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
ls /mnt/hgfs/


## (Opcional si se utiliza el còdigo de la rama nueva_rama) Limpiar archivo xml de caràcteres no validos
### Crear una copia de seguridad del archivo original
cp CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml.bak

### #Usar sed para eliminar caracteres no válidos
sed -i 's/[\x00-\x1F\x7F]//g' CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml


