# genrandimg
Generate random color images on Docker.

![](/example/example_512x512.png)

Run: 
```bash
git clone http://github.com/lunae-f/genrandimg/
cd genrandimg
docker build -t genrandimg .
docker run --rm -v "$(pwd):/app" genrandimg
docker run --rm -v "$(pwd):/app" genrandimg 1024 1024 nice_image_name.png   # Specify width, height, and filename
```