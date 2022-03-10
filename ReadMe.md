# WEBP Image Conversion Tool

A webp image converter that uses Google's webp converter. This must be installed prior to running. [Reference](https://developers.google.com/speed/webp/docs/cwebp)

This tool is designed to convert large batches of images to webp at a time. It provides the ability to convert a single file or an entire directory of images. 

Running to convert a single file:

```
$ python webp_convert.py -f image.png
```

Running to convert a directory:

```
$ python webp_convert.py -d image_dir
```
