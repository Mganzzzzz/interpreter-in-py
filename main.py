from tokenizer import Tokenizer

if __name__ == '__main__':
    with open('source.txt') as f:
        content = f.read()
        tokenizer = Tokenizer(content)
        ts = tokenizer.parse()
