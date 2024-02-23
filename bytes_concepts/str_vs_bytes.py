#!/usr/bin/env python3



def example_encode_decode():
    s = "Hello, world!"

    with open("data.txt","w",encoding="utf-8") as fp:
        fp.write(s)


    # for decode
    with open("data.txt", encoding="utf-8") as fp:
        print(fp.read())


if __name__ ==__name__:
    example_encode_decode()