# Warning!!!! Please change the port "49154" below for security
docker container rm -f pt_ssh
nvidia-docker run -d -p 49154:22 --name pt_ssh pytorch_ssh
