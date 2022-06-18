# Combine-Two-Arrays

This is a simple containerized script that will combine two arrays of sorted ints into a single sorted array.

To build the docker image, run the following command, substituting the tag if necessary (the code provided should be considered 1.0.0)

```
docker build . -t combine-two-arrays:<tag>
```

To run the image, you can use the following command (feel free to subsitute your own arrays)

```
docker run combine-two-arrays [1, 2, 7, 9] [3, 6, 8]
```
